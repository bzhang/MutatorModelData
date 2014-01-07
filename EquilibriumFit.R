dataPath = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
setwd(dataPath)
message(dataPath)
dirs = c("M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.15_AntiMutE0.15_EvlFrom1_Period1000", "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.2_AntiMutE0.2_EvlFrom1_Period1000", "M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1", "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.4_AntiMutE0.4_EvlFrom1_Period1000")
cmd1 = 'sed 1d '
cmd2 = " | awk -F '\t' '{print $3}'"
OutFile = paste(dataPath, 'Bootstrap_Equilibriums_015.txt', sep="")
for (dir in dirs[1]){
	cat(dir, file=OutFile, sep="", append=T)
	cat("\t", file=OutFile, sep="", append=T)
	setwd(dir)
	# setwd("1000pops")
	gens = seq(1, 71000, 1000)
	files = system('ls *_Pop.txt', intern=T)
	MutMat = matrix(ncol=length(gens), nrow=length(files))
	FileCount = 1
	for (file in files) {
		cmd = paste(cmd1, file, cmd2, sep="")
		MutRate = read.table(pipe(cmd))[,1]		
		MutMat[FileCount,] = MutRate
		FileCount = FileCount + 1
	}
	MeanMutRate = apply(MutMat, 2, mean)
	MeanMutRate = MeanMutRate * 0.05
	MeanMutRateEqui = MeanMutRate[40:length(MeanMutRate)]
	m = lm(MeanMutRateEqui ~ 1)
	pdf(paste(dir, "_MutRate_Equi.pdf",sep=""),height=10,width=12)
	par(mfrow=c(1,1),cex.axis=1.0, cex.lab=1.25, mar=c(5,5,2,2), bty="n")
	plot(gens, MeanMutRate, xlab="Generations", ylab="Mutation Rate", pch=16, cex=0.5, type='l')
	abline(m, col="blue")
	dev.off()
	setwd("..")
	cat(m$coefficients, file=OutFile, sep="", append=T)
	for (i in 1:10000) {
		cat("\t", file=OutFile, sep="", append=T)
		RandMeanMutRateEqui = sample(MeanMutRateEqui, size=length(MeanMutRateEqui), replace=T)
		# message(RandMeanMutRateEqui, sep="\t")
		m = lm(RandMeanMutRateEqui ~ 1) 
		cat(m$coefficients, file=OutFile, sep="", append=T)

	}
	cat("\n", file=OutFile, sep="", append=T)
}