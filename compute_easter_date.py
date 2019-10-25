


def compute_easter_date(year):
	
	n = year % 19;

	c = year // 100;
	u = year % 100;

	s = c // 4;
	t = c % 4;

	p = (c + 8) // 25;
	q = (c - p + 1) / 3;

	e = ((19 * n) + c - s - q + 15) % 30;

	b = u // 4;
	d = u % 4;

	L = ((2*t) + (2*b) - e - d + 32) % 7;
	
	h = (n + (11 * e) + (22 * L)) // 451;

	m = (e + L - (7 * h) + 114) // 31
	j = (e + L - (7 * h) + 114) % 31

	return m,j


def test_compute_date():

	annee_2006 = 2006
	result = compute_easter_date(annee_2006)
	print("mois {} jour {}".format(result[0], result[1]))


	annee_2030 = 2030
	result = compute_easter_date(annee_2030)
	print("mois {} jour {}".format(result[0], result[1]))

test_compute_date()

