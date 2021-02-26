library(dplyr)
library(flowCore)
livefi = read.csv("FileInfoLive.csv")
handgatedfi = read.csv("HandGatedFileInfo.csv")
dir.create("POISED_labels")
for (id in livefi$ID){
  message(id)
  allgd = dplyr::filter(handgatedfi,ID == id & cell_type != "NKT")
  allLi = dplyr::filter(livefi,ID == id)
  fcs = read.FCS(as.character(allLi$fpath), truncate_max_range = FALSE)
  expr = exprs(fcs) 
  rownames(expr) = 1:dim(expr)[[1]]
  output = data.frame()
  output2 = data.frame()
  for (i in 1:length(allgd$fpath)){
    hd = allgd$fpath[i]
    fc = read.FCS(as.character(hd),truncate_max_range = FALSE)
    cells = exprs(fc)
    #message(paste(allgd$cell_type[i],"..", dim(cells)[[1]]))
    message(".")
    ex = as_tibble(rbind(expr, cells)) ## merging all live cells with one hangated cell type for this sample 
    YesOrNo = duplicated(ex) | duplicated(ex, fromLast = TRUE) ## check for TRUE i.e. duplicated rows these are the gated cell type 
    YesOrNo = YesOrNo[1:dim(expr)[[1]]] ## removing the indexes of handgated cells 
    indexes = which(YesOrNo, TRUE) ## indexes of live cells that were gated out for this cell type
    cellType = allgd$cell_type[i] ## the cell type name
    if ( length(indexes) > 0) {
    tmp=data.frame("Index"=indexes,
      "CellType" = cellType)
    output = rbind(output,tmp) ## merging the temporary data frame to main output dataframe
	  }
  }
  message("finding..ungated..")
  ## check for some cells that are assigned to more than 1 cell type.
  YesOrNo = duplicated(output$Index) | duplicated(output$Index, fromLast = TRUE)
  uindexes = output$Index[which(YesOrNo, TRUE)]
  
  message(paste(length(uindexes), "cells .. found problamatic so marked as ungated"))
  output2 = dplyr::filter(output, !Index %in% uindexes)
  remaining = setdiff(rownames(expr),as.character(output2$Index)) ## those indexes not the part of any gated cell type were ungated
  tmp=data.frame("Index"=remaining,
                 "CellType" = "Unknown")
  output2 = rbind(output2,tmp) ##
  output2 <- output2[order(as.numeric(output2$Index)),]
  if (dim(expr)[[1]] == dim(output2)[[1]]){
  write.csv(output2,file = paste("POISED_labels/", id,"labels.csv",sep="."), quote = F, row.names = F)
  } else {
    message("Error .. some problem ")
  }
}


