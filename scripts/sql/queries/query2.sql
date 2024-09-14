with customer_total_return as
         (select sr_customer_sk   as ctr_customer_sk
               , sr_store_sk      as ctr_store_sk
               , sum(sr_return_amt) as ctr_total_return
          from cassandra.c_bigdata.store_returns
             , postgres.p.date_dim
          where sr_returned_date_sk = d_date_sk
            and d_year = 2000
          group by sr_customer_sk
                 , sr_store_sk)
select c_customer_id
from customer_total_return ctr1
   , redis.r.store
   , redis.r.customer
where ctr1.ctr_total_return > (select avg(ctr_total_return) * 1.2
                               from customer_total_return ctr2
                               where ctr1.ctr_store_sk = ctr2.ctr_store_sk)
  and s_store_sk = ctr1.ctr_store_sk
  and s_state = 'TN'
  and ctr1.ctr_customer_sk = c_customer_sk
order by c_customer_id