int* a = new int(1);
int* b = a;
a = new int(2);
cout << *b << endl;   // prints 1