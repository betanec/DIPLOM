
Matrix operator*(const Matrix& m1, const Matrix& m2)
{
	Matrix res;
	for (std::size_t i = 0; i < 4; i++) {
		std::slice row(i*4, 4, 1);
		for (std::size_t j = 0; j < 4; j++) {
			std::slice col(j, 4, 4);
			res._matrix[j + i*4] = (m1._matrix[ row ] * m2._matrix[ col ]).sum(); 
		}
	}
	return res;
}

Point Matrix::operator()(Point point) const
{
	std::valarray<double> vec = {point.x(), point.y(), point.z(), 1.};

	double x = (_matrix[ std::slice(0, 4, 1) ] * vec).sum(); 
	double y = (_matrix[ std::slice(4, 4, 1) ] * vec).sum(); 
	double z = (_matrix[ std::slice(2*4, 4, 1) ] * vec).sum(); 
	return Point(x, y, z);
}

Vector Matrix::operator()(Vector vector) const
{
	Point begin = this->operator()(Point(0,0,0));
	Point end = this->operator()(Point(vector.x(), vector.y(), vector.z()));

	return Vector(begin, end);
}


