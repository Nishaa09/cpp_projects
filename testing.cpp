#include <iostream>
using namespace std;

class item{
	public:
	string name;
	int item;
	float price;
	
    void getitem()
    {
    	cout<<"name of the item:";
    	cin>>name;
    	cout<<"quantity:";
    	cin>>item;
    	cout<<"price of the item:";
    	cin>>price;
	}
	float totalprice()
	{
		return item*price;
	}
	
};
class invoice{
	int noitem;
	item items[20];
	
	public:
		int i;
		invoice(int n)
		{
			noitem=n;
		}
		void createinvoice()
		{
		
	    for(i=0;i<noitem+1;i++)
	    {
	    	items[i].getitem();
	    	
		}
	    }
		
		
};

int main()
{
int noitem;
cout<<"how many items you have purchased:";
cin>>noitem;
invoice invoice(noitem);
invoice.createinvoice();
}