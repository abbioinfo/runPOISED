library(dplyr)


livefi=read.csv("FileInfoLive.csv")
handgatedfi = read.csv("HandGatedFileInfo.csv")


# randomly select 20 samples from IDs ##
IDs = livefi[sample(1:dim(livefi)[[1]], 20, replace = F), ]$ID
# randomly select 3 samples from remining IDs ##
oIDs = setdiff(livefi$ID,IDs)
##### select all handgated FCS files for these 3 samples ##
threeIDs = oIDs[sample(1:length(oIDs),3, replace = F)]


traininglive = dplyr::filter(livefi, ID %in% threeIDs)
traininggated = dplyr::filter(handgatedfi, ID %in% threeIDs)
testinglive = dplyr::filter(livefi, ID %in% IDs)

colnames(traininglive) = c('fpath','sample_id','Source','ID')
colnames(testinglive) = c('fpath','sample_id','Source','ID')
colnames(traininggated) = c('fpath','sample_id','cell_type','Source','ID')

write.csv(file="TrainingDataset_live.csv", traininglive[,c('fpath','ID')], quote = F, row.names=F)
write.csv(file="TrainingDataset_manuallygated.csv", traininggated[,c('fpath','cell_type','ID')], quote = F,row.names=F)
write.csv(file="TestingDataset_live.csv", testinglive[,c('fpath','ID')], quote = F, row.names=F)







             
             
