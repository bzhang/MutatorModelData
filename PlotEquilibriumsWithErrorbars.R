library('Hmisc')
dataPath = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
setwd(dataPath)
message(dataPath)
files = system('ls Bootstrap_*.txt', intern=T)
u = c()
ups = c()
lows = c()
file_id = 1

for (file in files) {
	data = read.table(file, sep="\t")
	data = data[2:length(data)]
	u[file_id] = apply(data, 1, mean)
	qs = quantile(data, probs=c(0.025, 0.975))
	ups[file_id] = qs[1,2]
	lows[file_id] = qs[1,1]
	file_id = file_id + 1
}


errbar(c(0.15, 0.2, 0.3, 0.4), u, ups, lows, xlab="Mutator/Anti-mutator Effects", ylab="Mutation Rate at Equilibrium", bty="l")
abline(h=0.1, col='blue')
lines(c(0.15, 0.2, 0.3, 0.4), u)
