dataPath = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/M0.0_R0.0_G70000_N10000_BeneMR4.0E-4_DeleMR0.2_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1_Period1000"
setwd(dataPath)
message(dataPath)
getwd()
files = system('ls *_Pop.txt', intern=T)
cmd1 = 'sed 1d '
cmd2 = " | awk -F '\t' '{print $3}'"
file_count = 0
line_num = 10
colors = rainbow(line_num)
plot(NA, xlim=c(0, 70), ylim=c(0, 2))
for (file in files) {
	file_count = file_count + 1
	message(file_count)
	cmd = paste(cmd1, file, cmd2, sep="")
	MutRate = read.table(pipe(cmd))[,1]
	lines(seq(0, 70), MutRate, pch=16, type='l', lty=1, cex=0.5, col=colors[file_count])
	if (file_count >= line_num) break
}