#include <iostream>
 using namespace std;
 
 class item{
       string name;
       int item;
       double price;
       
       public:
              void getitem(string n,int i,double p);
              {
                   name = n;
                   item = i;
                   price = p;
                   }  
                   
              void putitem(void);
              {
                   cout<<"name of idea:"<<name<<endl<<"no of iteam:"<<item<<endl<<"price od iteam:"<<price<<endl;
                   }
                   };   
                   
                   
int main()
{
   iteam i;
   i.getitem(macbook,1,79000.50);
   i.putitem();
   return 0;
   
}                                       
