# Deprecated algorithm
rm(list=ls())
dataPath = "/Volumes/BigTwins/MutatorModelData/N1000/Sexual/FixedR1.0/"
setwd(dataPath)
dirs = system('ls -d */', intern=T)
output = paste(dataPath, "AdaptationRates.txt", sep="")
windowSize = 1000
step = 10
for (dir in dirs) {
	message(dir)
	setwd(paste(dataPath, dir, sep=""))
	cat(dir, file=output, append=T)
	cat("\t", file=output, append=T)
	files = system('ls *_Pop.txt', intern=T)
	cmd1 = 'sed 1d '
	cmd2 = " | awk -F '\t' '{print $2}'"
	file_count = 0
	for (file in files) {
		file_count = file_count + 1
		message(file_count)
		cmd = paste(cmd1, file, cmd2, sep="")
		fitness = read.table(pipe(cmd))
		gens = seq(1, 20000, 1)
		rates = c()
		# for (i in (1:(length(fitness[,1])-windowSize))) {
		for (i in seq(1, length(fitness[,1])-windowSize+1, step)) {
			message(i)
			m = lm(fitness[i:(i+windowSize-1), 1] ~ gens[i:(i+windowSize-1)])
			rates = c(rates, coef(m)[2])
		}
		cat(max(rates), file=output, append=T)
		cat("\t", file=output, append=T)
	}
	cat("\n", file=output, append=T)
}
