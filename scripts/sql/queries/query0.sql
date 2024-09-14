select cd.cd_purchase_estimate, c.c_first_name, c.c_last_name
from redis.r.customer_demographics cd,
     redis.r.customer c
where c.c_current_cdemo_sk = cd.cd_demo_sk
limit 100;

with inv_sum as (select i.i_item_sk, i.i_product_name, sum(inv.inv_quantity_on_hand) as total
                 from postgres.p.item i,
                      postgres.p.inventory inv
                 where inv.inv_item_sk = i.i_item_sk
                   and inv.inv_quantity_on_hand IS NOT NULL
                 group by i.i_item_sk, i.i_product_name)
select i_item_sk, i_product_name, total
from inv_sum
where total = (select max(total) from inv_sum);


select i.i_item_sk, i.i_product_name, sum(inv.inv_quantity_on_hand) as total
from postgres.p.item i,
     postgres.p.inventory inv
where inv.inv_item_sk = i.i_item_sk
  and inv.inv_quantity_on_hand IS NOT NULL
group by i.i_item_sk, i.i_product_name
order by total desc
limit 1;





select i_product_name, i_item_sk, cnt
from postgres.p.item,
     (select inv_item_sk, count(*) as cnt
      from (select distinct inv_warehouse_sk, inv_item_sk
            from postgres.p.inventory
            where inv_quantity_on_hand > 0)
      group by inv_item_sk)
where i_item_sk = inv_item_sk

select i_item_sk, i_product_name, i_current_price
from postgres.p.item
where i_current_price > 5 and  i_current_price < 10

select ss_ticket_number, ss_item_sk, ss_net_paid from cassandra.c_bigdata.store_sales where ss_net_paid > 10000;

select s.ss_ticket_number, s.ss_item_sk, i.i_product_name, i.i_current_price, s.ss_net_paid
from cassandra.c_bigdata.store_sales s, postgres.p.item i
where s.ss_net_paid > 10000 and s.ss_item_sk = i.i_item_sk
limit 10000;