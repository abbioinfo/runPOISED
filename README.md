## Vignette
Replicating results of orignal manuscript from POISED dataset

# 1. About POISED dataset
POISED dataset (Chinthrajah et al., 2019)) includes 30 CyTOF samples from human PBMCs of peanut-allergic individuals, for testing or benchmarking the CyAnno algorithm. For more information please refer [#1](https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(19)31793-3.pdf) and [#2](https://www.biorxiv.org/content/10.1101/2020.08.28.272559v1) 

# 2. Dataset design
The dataset consists of 30 CyTOF samples with a panel of 39 marker (21 lineage + 18 functional markers), in which 15 samples were peanut stimulated and 15 samples were untreated. These samples were processed across 7 batches and 21 cell types were manually gated (including closely related cell types as well as non-canonical rare cell types).The non-canonical peanut reactive T cells used in this study were CD69+ CD40L+ CD4+ T cells and CD69+ CD8+ T cells (Neeland et al., 2020). Cells not the part of any of the 21 gated cell population are labelled as "Unknown", this may includes "ungated" cells or cells with "unknown" phenotype.

# 3. Dataset availability
Raw unlabeled POISED dataset files in FCS 3.0 format and normalized labelled CSV format can be obtained from [FlowRepository](https://flowrepository.org/) (FR-FCM-Z2V9; temporarily restricted for public access). Howevever, for executing CyAnno on POISED dataset and replicating results of the orignal manuscript, unnormalized FCS files of "manually gated" cell types (training dataset) as well as "unlabelled" live cells (test dataset) can be obtained using the instructions available in section 4.1.

# 4. CyAnno: Step by Step instructions
Please follow to the instructions to train the CyAnno models using just 3 POISED CyTOF samples and label the cell from 20 different POISED CyTOF samples. In theory, 3 or more samples should be enough to train CyAnno in order to label the live cells from (any number of) "unlabelled" samples, given training samples are not significantly different from "unlabelled" samples, in terms of marker expression profile due to batch effects, external stimulation(s) or any other factor.

*Important*: Make sure if you have installed [Git-LFS](https://git-lfs.github.com/) installed in $PATH of your working directory. You may use one of the following commands to install to Git-LFS:

**Homebrew**: 
```brew install git-lfs```

**MacPorts**: 
```port install git-lfs```

**ubuntu/debian**: 
```sudo apt install git-lfs```


More details about the installation can be found [here](https://github.com/git-lfs/git-lfs).

### 4.1 Step 1: Clone the repository and download the POISED dataset

```
git clone https://github.com/abbioinfo/runPOISED.git
cd runPOISED


```

