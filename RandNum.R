prob = 0.9
exp_mean = 0.05
gaussian_mean = 10
rands = c()
for (i in 1:100000) {
	r = runif(1)
	if (r < prob) {
		rands = c(rands, rexp(1, rate=1/exp_mean))
	} else {
		rands = c(rands, rnorm(1, mean=gaussian_mean, sd=0.01))
	}
}
hist(rands)
mean(rands)
sd(rands)