## area_numbers.csv process
* pd.read_html - had to use dummy value in thousands parameter to make comma separated values behave correctly
* The area numbers on the site don't look completely accurate. Found pdf that contradicted the official site, but not sure which is correct.

---

## highest_group_numbers.csv process
* Was going to use pd.read_html again, but requires table so I used pd.read_csv
* Tried to identify data rows with \t, but not all data rows had it. Spacing used in data rows is **VERY** inconsistent.
* Having to use spaces as separators required the messy appending to the DataFrame. Definitely needs clean up.

---

## group_number_order.csv process
* Just used the csv package because pandas seemed like overkill