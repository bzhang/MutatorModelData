rm(list=ls())
dataPath = "/Volumes/BigTwins/MutatorModelData/Core_Expo_M0.0_R0.0_G600000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03/"
setwd(dataPath)

files = system('ls *_Pop.txt', intern=T)
cmd1 = 'sed 1d '
cmd2_dele = " | awk -F '\t' '{print $6}'"
cmd2_bene = " | awk -F '\t' '{print $8}'"
cmd2_fitness = " | awk -F '\t' '{print $2}'"
x = seq(0,599999)
bene_coef = matrix(nrow = length(files), ncol = 3)
dele_coef = matrix(nrow = length(files), ncol = 3)
row_count = 1
for (file in files){
	cmd_dele = paste(cmd1, file, cmd2_dele, sep="")
	cmd_bene = paste(cmd1, file, cmd2_bene, sep="")
	dele = read.table(pipe(cmd_dele))
	bene = read.table(pipe(cmd_bene))
	qmodel_dele = lm(dele[,1] ~ x + I(x^2))
	bene_coef[row_count,] = qmodel_dele$coefficients
	qmodel_bene = lm(bene[,1] ~ x + I(x^2))
	dele_coef[row_count,] = qmodel_bene$coefficients
	row_count = row_count + 1
}

mean_dele = apply(dele_coef, 2, mean, na.rm=T)
var_dele = apply(dele_coef, 2, var, na.rm=T)
mean_bene = apply(bene_coef, 2, mean, na.rm=T)
var_bene = apply(bene_coef, 2, var, na.rm=T)




