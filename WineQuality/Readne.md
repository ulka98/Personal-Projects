# Wine Quality

## This project has notebooks depicting the Problem statements below. These are very basic notebooks based on analysis.

Dataset name: winequality-red.csv
 
__Problem Statement 1)__ Plot Hist and Line graph for pH level for Quality 5 and Quality 8
 
__Problem Statement 2)__ Which quality of wine is highly acidic?

__Problem Statement 3)__ Quality vs Total Acidity Bar and Pie chart

__Problem Statement 4)__ 

1.SO2 is Considered to be harmful of health. So which wine is most harmful for your health? Provide rank on the degree of harmfulness of wines and plot a graph for SO2 vs Quality.

2.Find the correlation between residual sugar vs total sulphur dioxide. Plot three scatter plots for quality range (3, 4), (5, 6), (7, 8).
		      
Fact: Sweet white wines typically contain the most sulphites, as more is added to halt the fermentation process.Another reason why a night on the white might make that hangover worse than usual.
__Expected Analysis__: Relation is directly proportional. Some medium and low-quality wines have high amounts of both contents.

3. Find a correlation between pH and Quality. 

Fact: Winemakers use pH as a way to measure ripeness in relation to acidity. Low-pH wines will taste tart and crisp, while higher-pH wines are more susceptible to bacterial growth. Most wine pH's fall around 3 or 4; about 3.0 to 3.4 is desirable for white wines, while about 3.3 to 3.6 is best for red.

__Expected analysis__: Higher quality wines should contain pH between 3 and 3.4

4. pH vs residual sugar. 
		      
Fact: The perfect way to contextualize how sweetness reduces the sensation of acidity in wine is to compare how you react to tasting a raw lemon to Coca-Cola. Technically, they have the same pH (around 2.5), but since coke is sweet it is not as intense. 
		      
__Expected analysis__: Should have indirect proportion (For saving the plots use : plt.savefig('filename.jpg'))
