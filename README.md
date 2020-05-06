# bst263-final-project
Final project for BST263 Statistical Learning 

## Background
Chest computerized tomography (CT) has been used in a few countries as a preliminary diagnostic tool for COVID-19 where availability of reverse transcription polymerase chain reaction (RT-PCR) tests was limited. However, current CT-based diagnosis is largely based on review of the imaging result by healthcare professionals. Latest study showed that using RT-PCR test as the gold standard, the physician review of chest CT scan has a sensitivity of 97% and specificity of 75%[Ai et al, 2020]. One recent publication utilized a deep learning network (COVID-Net) performed under an enhanced processor to distinguish COVID-19 and community acquired pneumonia patients based solely on their CT scan data. This algorithm achieved higher specificity (96%) but lower sensitivity (90%) than physician review of chest CT images [Li et al, 2020]. 

## Aim
We aim to evaluate whether machine learning can improve prediction accuracy in classifying COVID-19 cases vs non-COVID-19 cases using lung CT images. We are especially interested in whether it’s possible to increase sensitivity above 90% given the same specificity level at around 96%.    

## Data source
We will utilize the CT-scan dataset put together by researchers at University of California, San Diego (UCSD) [https://github.com/UCSD-AI4H/COVID-CT]. This is a growing open-source dataset with CT images extracted from peer-reviewed or pre-print publications, with confirmatory RT-PCR test for COVID-19.  Currently the raw data contains 350 CT scans taken at various time points for 216 patients with confirmed COVID-19 and 397 CT scans taken at various time points for 91 patients with non-COVID-19 diagnosis. Age and gender information are available for some but not all patients with confirmed COVID-19. 

## Image Processing 
Most of the CT scans downloaded are in 3 dimensions, which are CT images colored annotated by either doctors or researchers. Since raw CT scans are already in greyscale, and to maximally resemble real life scenarios, we first transformed all images to black and white versions. Since all pictures have different dimensions, to avoid information loss to the greatest extent, we first made all pictures portrait mode and then crop all to make their dimension the same as the smallest image found. Then we obtained the gradient field and extracted the feature vectors by partitioning the height and width into 16 partitions each, and then partition each angle into 32 intervals. 	

## Classification
We will first split the CT image dataset into a training dataset (80%) and a test dataset (20%). In the training sample, we will apply the following classification methods: support vector machine, random forest, L1-penalized logistic regression, linear discriminant analysis, quadratic discriminant analysis and gradient boosting. We will train the models using 10-fold cross validation. We will then assess model performance in the test dataset by computing test accuracy, sensitivity and specificity for each model. The model that yields the highest test accuracy and sensitivity without major compromise on specificity will be chosen as the final model. 	

## Benchmark method
 
The researchers at University of California, San Diego (UCSD) had already utilized this COVID-CT datasets to construct two neural network models for us to benchmark with. Since this is a relatively small collection of images, they used transfer learning and data augmentation to avoid overfitting and mitigate data inefficiency. Transfer learning was based on the network trained in ChestX-ray14 [3] dataset released by NIH, and then fine tuned on the COVID-19 dataset. The second network model utilized data augmentation to mitigate data efficiency: by creating new image-label pairs and adding the synthesized pairs into the training set. Data augmentation includes random affine transformation, random crop and random flip. Two methods had reached accuracy of 84% and 91%, respectively.
 
 
## References 
 [1] Ai T, Yang Z et al. Correlation of Chest CT and RT-PCR Testing in Coronavirus Disease 2019 (COVID-19) in China: A report of 1014 cases. Radiology. 0(0). Feb 26, 2020. https://doi.org/10.1148/radiol.2020200642

 [2] Li L, Qin L et al. Artificial Intelligence Distinguishes COVID-19 from Community Acquired Pneumonia on Chest CT. Radiology.0(0). Mar 19, 2020. https://doi.org/10.1148/radiol.2020200905
 
 [3] Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi Bagheri, and Ronald M Summers. Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on weaklysupervised classification and localization of common thorax diseases. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 2097–2106, 2017
