# imported a package that contained the datasets. 
import familiar

# Imported the 1 Sample T-Test
from scipy.stats import ttest_1samp

# Imported the 2 Sample T-Test
from scipy.stats import ttest_ind

# Imported the Chi-Squared Test
from scipy.stats import chi2_contingency

# Saved the 'vein' package to the vein_pack_lifespans variable. the package is from the familiar.py file.
vein_pack_lifespans = familiar.lifespans(package='vein')

# Performed the 1 Sample T-Test 
vein_pack_test = veins, pval = ttest_1samp(vein_pack_lifespans, 71)

# Used an if else statement based on the p-value after the 1 Sample T-Test has been performed.
if (pval < 0.05):
    "The Vein Pack Is Proven To Make You Live Longer!"
else:
    "The Vein Pack Is Probably Good For You Somehow!"

# Saved the 'artery' package to the artery_pack_lifespans variable. the package is from the familiar.py file.
artery_pack_lifespans = familiar.lifespans(package='artery')

# Performed a 2 Sample T-Test
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

# Used an if else statement based on the p-value after the 2 Sample T-Test test has been performed
if (pval < 0.05):
    "the Artery Package guarantees even stronger results!"
else:
    "the Artery Package is also a great product!"

# This table is from the familiar package. calculates low, medium and high levels of iron for veins and artery.
iron_contingency_table = familiar.iron_counts_for_package()

# Performed a chi-squared test 
iron_pvalue = chi2, iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)

# Used an if else statement in relation to the p-value after the chi-square test has been performed
if (pval < 0.05):
    "The Artery Package Is Proven To Make You Healthier!"
else:
    "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"

print pval
print package_comparison_results
print iron_pvalue
