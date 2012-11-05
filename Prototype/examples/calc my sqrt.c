1    = 1                 1
4    = old + 2*1 + 1     2
9    = old + 2*2 + 1     3
16   = old + 2*3 + 1     4
25   = old + 2*4 + 1     5


abdfh
bcdfh
ddefh
fffgh
hhhhi

---

unsigned Input = 29;
unsigned Counter = 0;
unsigned Old = 0;

while(true)
{
	// TODO< optimize this >
	Old = Old + 2*Counter + 1;

	if( Old >= Input )
	{
		break;
	}

	Counter++;
}

// now the result is in Counter
