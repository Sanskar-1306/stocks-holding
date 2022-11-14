from posixpath import split
from django.db import models
from decimal import Decimal
# Create your models here.

class Stock(models.Model):
    """Data model for stock data"""
    
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    time = models.TimeField(auto_now_add=True)

class TransactionModel(models.Model):
    """ Model for the transaction table"""
    
    company_name = models.CharField(max_length = 50)
    trade_type = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    cummulative_allocation = models.DecimalField(max_digits=10,decimal_places=2)
    bal_quantity = models.DecimalField(max_digits=10,decimal_places=2)
    avg_purchase_price = models.DecimalField(max_digits=10,decimal_places=2)


    """ overriding the save function for our required used case"""
    def save(self, *args, **kwargs):
        
        last_element = TransactionModel.objects.all().last() if TransactionModel.objects.count()>0 else None
        print(TransactionModel.objects.count())
        print(last_element)
        self.amount = self.quantity*self.price
        
        new_bal_quantity = last_element.bal_quantity if last_element!=None else 0
        new_cummulative = Decimal(last_element.cummulative_allocation) if last_element!=None else 0 
        
        if self.trade_type =="BUY":
            """ storing stock in db and increasing the balance quantity and cummulative accumulation"""
            s = Stock(quantity = self.quantity, price = self.price)
            s.save()
            new_bal_quantity+=self.quantity
            new_cummulative+=Decimal(self.amount)
            



        elif self.trade_type == "SELL":
            q = self.quantity
        
            """sorting the stocks in order of time and accordingly removing them from the db and 
              updating the new cuumulative accumulation and balance quantity"""
            stocks = Stock.objects.all().order_by('time')
            for stock in stocks:
                if stock.quantity<=q:
                    q-=stock.quantity
                    new_bal_quantity-=stock.quantity
                    new_cummulative-=stock.quantity*stock.price
                    stock.delete()

                else:
                    stock.quantity-=q
                    new_bal_quantity-=q
                    new_cummulative-=q*stock.price
                    stock.save()
                    break    
                if q==0:
                    break

        
        elif self.trade_type == "SPLIT":
            split_ratio = self.quantity/last_element.bal_quantity
            new_bal_quantity = self.quantity
            new_cummulative = last_element.cummulative_allocation
            for stock in Stock.objects.all():
                stock.price/=split_ratio
                stock.quantity*=split_ratio
                    

        self.avg_purchase_price = new_cummulative/new_bal_quantity
        self.bal_quantity = new_bal_quantity
        self.cummulative_allocation = new_cummulative

        super(TransactionModel, self).save(*args, **kwargs)
       
 
