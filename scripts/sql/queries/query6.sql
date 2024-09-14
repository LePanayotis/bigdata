select c_last_name
     , c_first_name
     , c_salutation
     , c_preferred_cust_flag
     , ss_ticket_number
     , cnt
from (select ss_ticket_number
           , ss_customer_sk
           , count(*) cnt
      from cassandra.c_bigdata.store_sales,
           postgres.p.date_dim,
           redis.r.store,
           redis.r.household_demographics
      where ss_sold_date_sk = d_date_sk
        and ss_store_sk = s_store_sk
        and ss_hdemo_sk = hd_demo_sk
        and (d_dom between 1 and 3 or date_dim.d_dom between 25 and 28)
        and (hd_buy_potential = '>10000' or
             hd_buy_potential = 'Unknown')
        and hd_vehicle_count > 0
        and (case
                 when hd_vehicle_count > 0
                     then hd_dep_count / hd_vehicle_count
                 else null
          end) > 1.2
        and d_year in (1999, 1999 + 1, 1999 + 2)
        and s_county in ('Williamson County')
      group by ss_ticket_number, ss_customer_sk) dn,
     redis.r.customer
where ss_customer_sk = c_customer_sk
  and cnt between 15 and 20
order by c_last_name, c_first_name, c_salutation, c_preferred_cust_flag desc, ss_ticket_number;

