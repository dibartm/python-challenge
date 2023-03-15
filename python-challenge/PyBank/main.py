# open csv
f=open("budget_data.csv")
# read in header line
f.readline()
# intialize : month_count , total_profit_loss , maximus_increase_amount , maximun_increase_date
# intialize : min_increase_amt , min_increase_date , year = 2013
month_count = 0
total_profit_loss = 0
maximus_increase_amount = 0
maximun_increase_date = 0
min_increase_amt = 0
min_increase_date = 0
year = 2013
net_changes=0
last_profit=0
#for each line split into date and profit
print(f)
for line in f:
    line=line.strip()
    line=line.split(",")
    
    date = line[0]
    profit = int (line[1])
    if month_count==0:
        net_changes=0
    else:
        print(profit,last_profit,net_changes)
        net_changes=net_changes+(profit-last_profit)
    
    # increment_month_count
    month_count = month_count + 1
    # add profit to total_profit_loss
    total_profit_loss = total_profit_loss + profit
    # print(month_count,total_profit_loss,net_changes,sep=" --> ")
    last_profit=profit
# caculate monthly proft change

# extract month abbreviation , if month is jan incr year

# update Max and Min amount and dates

# print out results

f.close()