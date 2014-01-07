rm(list=ls())
library(segmented)
dataPath = "/Volumes/BigTwins/MutatorModelData/N1000/Sexual/FixedR0.75/"
setwd(dataPath)
dirs = system('ls -d */', intern=T)
# dirs = c("M0.0_R0.0_G20000_N10000_BeneMR4.0E-6_DeleMR0.0020_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0_AntiMutMR0.0_MutaE0.1_AntiMutE0.1_EvlFrom100000_Period1", "M0.0_R0.0_G20000_N10000_BeneMR4.0E-5_DeleMR0.02_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0_AntiMutMR0.0_MutaE0.1_AntiMutE0.1_EvlFrom100000_Period1")
output = paste(dataPath, "AdaptationRates_LogFit_NoSeg.txt", sep="")
sink(output)
# windowSize = 1000
# step = 10
# cmd_ngen1 = "echo "
# cmd_ngen2 = " | cut -d '_' -f3 | cut -d 'G' -f2"

for (dir in dirs) {
	message(dir)
	# cmd_ngen = paste(cmd_ngen1, dir, cmd_ngen2, sep="")
	# n_gen = as.integer(system(cmd_ngen, intern=T))
	setwd(paste(dataPath, dir, sep=""))
	cat(dir, append=T)
	files = system('ls *_Pop.txt', intern=T)
	cmd1 = 'sed 1d '
	cmd2 = " | awk -F '\t' '{print $2}'"
	file_count = 0
	for (file in files) {
		file_count = file_count + 1
		message(file_count)
		cmd = paste(cmd1, file, cmd2, sep="")
		fitness = read.table(pipe(cmd))
		log_fitness = log(fitness[,1])
		gens = seq(1, length(log_fitness), 1)
		# rates = c()
		m <- lm(log_fitness ~ gens)
		# seg <- segmented(m, seg.Z = ~gens, psi=c(1000))
		pdf(paste(file, "_LogFit_NoSeg.pdf",sep=""),height=10,width=12)
		par(mfrow=c(1,1),cex.axis=1.0, cex.lab=1.25, mar=c(5,5,2,2), bty="n")
		plot(gens, log_fitness, xlab="Generations", ylab="Log Fitness", pch=16, cex=0.5)
		# plot(seg, add=T, col="red")
		abline(m, col="blue")
		dev.off()
		cat("\t", append=T)
		# cat(coef(seg)[3], append=T)
		cat(coef(m)[2], append=T)
	}
	cat("\n", append=T)
}
sink()