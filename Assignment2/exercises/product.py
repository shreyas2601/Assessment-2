import pandas as pd

data={
    'product_name':['memory card','pendrive','mobile','mouse','laptop'],
    'prices':[400,800,10000,300,25000],
    'category':["electronics",'electronics','electronics','electronics','electronics']
}
df=pd.DataFrame(data)

#price discount
df['price_discount']=df['prices']*0.9

#product less than 500

cheap_product=df[df['price_discount']<500]

print(cheap_product)