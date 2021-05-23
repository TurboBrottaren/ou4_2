#include <cstdlib>
// Integer class 

// """
// Solutions to module 4
// Student: Oskar Ekstrand
// Mail: oskar.ekstrand.1905@student.uu.se
// Reviewed by:
// Reviewed date: 
// """

class Heltal{
	public:
		Heltal(int);
		int get();
		int fib();
		void set(int);
			
	private:
		
		int val;
		int fibcpp(int);
	};
 
Heltal::Heltal(int n){
	val = n;
	}

int Heltal::fibcpp(int n){
    if (n <= 1)
        return n;
	else
    	return fibcpp(n-1) + fibcpp(n-2);
}

int Heltal::fib(){
	int n = val;
	return fibcpp(n);

}
 
int Heltal::get(){
	return val;
	}
 
void Heltal::set(int n){
	val = n;
	}
	
extern "C"{
	Heltal* Heltal_new(int n) {return new Heltal(n);}
	int Heltal_get(Heltal* heltal) {return heltal->get();}
	int Heltal_fib(Heltal* heltal) {return heltal->fib();}
	void Heltal_set(Heltal* heltal, int n) {heltal->set(n);}
	void Heltal_delete(Heltal* heltal){
		if (heltal){
			delete heltal;
			heltal = nullptr;
			}
		}
	}