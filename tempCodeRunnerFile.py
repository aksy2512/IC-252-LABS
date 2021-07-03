p=float(input("Write the probability for a successful transmission: "))
# p1=int(p*100)
# lst=[]
# for i in range(100):
#     if(i<p1):
#         lst.append(1)
#     else:
#         lst.append(0)
# values = []
# for i in range(10000):
#     count=0
#     x=0
#     while(x!=1):
#         x=random.choice(lst)
#         count=count+1
#     values.append(count)
# plt.title('Histogram for number of heads obtained')
# plt.ylabel('Count')
# plt.xlabel('Frequency of heads')
# plt.hist(values, bins=list(range(1,21)))
# plt.show()