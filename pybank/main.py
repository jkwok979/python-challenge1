import os
import csv
total_mth = 0
sum_rev = 0
total_chg = 0
cur_row = 1
grt_inc_rev = -10000000
grt_dec_rev = 10000000
csvpath = os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')
    reader=csv.DictReader(csvfile)
    #csvreader =csv.reader(csvfile)
    #csv_header = next(csvreader)
    print('Financial Analysis')
    print('----------------------------')
    for row in reader:
        if cur_row > 1:       
            last_mth_rev = this_mth_rev
        this_mth_rev = float(row['Revenue'])
        if cur_row > 1:
            chg_mth = this_mth_rev - last_mth_rev
            total_chg = total_chg + chg_mth
            if chg_mth > grt_inc_rev:
                grt_inc_rev = chg_mth
                mth_grt_inc_rev = row['Date']
            if chg_mth < grt_dec_rev:
                grt_dec_rev = chg_mth
                mth_grt_dec_rev = row['Date']    
        sum_rev = sum_rev + this_mth_rev
        total_mth = total_mth + 1
        cur_row += 1
print("Total Months:",total_mth)
print("Total: $",sum_rev)
print("Average Change: $",round((total_chg/(total_mth-1)),2))
print("Greatest Increase in Profits: ",mth_grt_inc_rev, ' ($',int(grt_inc_rev),')')
print("Greatest Decrease in Profits: ",mth_grt_dec_rev, ' ($',int(grt_dec_rev),')')
text='Total Months: '+str(total_mth)+'\nTotal: $'+str(sum_rev)
text=text+'\nAverage Change: $'+str(total_chg/(total_mth-1))
text=text+'\nGreatest Increase in Profits: '+ str(mth_grt_inc_rev)+' ($'+str(int(grt_inc_rev))+')'
text=text+'\nGreatest Decrease in Profits: '+ str(mth_grt_dec_rev)+' ($'+str(int(grt_dec_rev))+')'
savefile= open('pybankout.txt','w')
savefile.write(text)
savefile.close()