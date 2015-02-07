#include <string>


#define BOOST_ALL_DYN_LINK
#define A_CONSTAND 5


#ifdef BOOST_ALL_DYN_LINK
int main(void)
{
	return 0;
}
#else
const esp = 8;
#endif
