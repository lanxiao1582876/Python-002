# 翻译mysql语句
import pandas as pd
import numpy as np
tips = pd.read_excel(r'tips.xlsx')
#1. SELECT * FROM data;
tips
# 2. SELECT * FROM data LIMIT 10;
tips.head(10)
#3. SELECT id FROM data;  //id 是 data 表的特定一列
tips['id']
#4. SELECT COUNT(id) FROM data;
tips['id'].shape[0]

#5. SELECT * FROM data WHERE id<1000 AND age>30;
tips[(tips['id'] < 1000) & (tips['age'] >30)   ]

#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
#DISTINCT 删除重复行
tips.groupby('id').agg({'order_id': pd.Series.nunique})

#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
output = pd.merge(table1, table2, on='id')
#或
pd.merge(table1, table2, left_on= 'id', right_on='id')

#8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2])

#9. DELETE FROM table1 WHERE id=10;
# 列出不能id不等于10的
tips.loc[tips['id'] != 10]

#10. ALTER TABLE table1 DROP COLUMN column_name;
tips.drop('id',axis = 1)


