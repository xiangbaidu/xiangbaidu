#--*-- coding:uft-8 --*--
print("hillo,world")
print("--------------------------------")


str='''
#2618159318630820999994
#0936392128482094399891
#0546390942099342789397
#2434422742950999951599
#2126782594639322949632
#0346542526959350959999
#2718300442151799789999
#2652540352952518912495
#1220540406950294489928
#1344120552951306099393
#0244691220399394090999
#0226272212661320990294
#0926122436511752819994
#2146662394092518959397
#0536091740099352549992
#0444392142950906639397
#2344481036780294669398
#1534270920271244991791
#2726549318399394279942
#2244662348950294999399
#1208752240309994309996
#2536420994782091992699
'''
for a in str:
  print(a)

print("thank you !")
sum=0
for a in str:
  if '\n' in a:
    continue;
  sum +=int(a)
print('-----------end----------')
print(sum)
  
