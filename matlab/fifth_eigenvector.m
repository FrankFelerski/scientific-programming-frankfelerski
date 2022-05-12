% Test comment
five_ones = ones(1,5)
five_twos = 2*five_ones
m1 = diag(five_twos)
four_ones = ones(1,4)
four_negative_ones = -1*four_ones
n1 = diag(four_negative_ones)
m2 = [[zeros(1,4); n1] zeros(5,1)]
m3 = m2'
m4 = m1 + m2 + m3
m5 = m4*(1/(2*(1/(5+1))^2))

e = eig(m5)
[V,D] = eig(m5)
fifth_eigen_vector = -V(:,1)
fifth_eigen_value = D(5,5)

% xvalues = linspace(1/(5+1),5/(5+1), 5)
x = [0.1667, 0.3333, 0.5000, 0.6667, 0.8333]
x3 = [0:.1:1]
y = sqrt(2)*sin(pi*x3)
plot(x3,y,':', x, fifth_eigen_vector, '--')
xlabel =('x')
ylabel = ('eigen_vectors')
