# 基金信息表
create table fund_info(
                        id bigint not null auto_increment key,
                        name varchar (32) unique,
                        num varchar (20) unique
)character set 'utf8',engine='InnoDB';

# 基金净值表
create table fund_jz(
                        id bigint not null auto_increment key,
                        fund bigint,
                        jzdate varchar(15),
                        dwjz decimal(10,4),
                        ljjz decimal(10,4),
                        jzzzl decimal(5,2),
                        foreign key(fund) references fund_info(id)
)character set 'utf8', engine='InnoDB';

# 定投表




create table fixed_invest(
                          id bigint not null auto_increment key,
                          fund bigint,
                          jzdate varchar(15),
                          last_dwjz decimal(10,4),
                          plan_money decimal(10,2),
                          fact_money decimal(10,2),
                          yesterday_earn decimal(10,2),
                          total_earn decimal(10,2),
                          earn_rate decimal(5,2),
                          foreign key(fund) references fund_info(id)
)character set 'utf8', engine='InnoDB'