select *
from
  (SELECT row_number() over (PARTITION BY ss_store_sk
                             ORDER by money_spent_in_current_value desc) as row_num,
                            *
   FROM
     (SELECT ss.ss_store_sk,
             c.c_customer_sk,
             sum(i.i_current_price * ss_quantity) as money_spent_in_current_value
      FROM cassandra.c_bigdata.store_sales ss,
           redis.r.customer c,
           postgres.p.item i
      WHERE c.c_customer_sk = ss.ss_customer_sk
        and ss.ss_item_sk = i.i_item_sk
      GROUP BY ss.ss_store_sk,
               c.c_customer_sk))
where row_num < 4
order by ss_store_sk,
         row_num;

