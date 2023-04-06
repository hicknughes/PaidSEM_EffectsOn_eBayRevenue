#Overview
An analysis of paid SEM marketing on eBay revenues across 210 'designated market areas' using 1)Difference in difference, 2)Synthetic Controls and 3)Synthetic Difference in Difference analyses

###The Data
This dataset includes 210 ‘designated market areas’ (DMAs) in the United States. In 2012, a team
of researchers (Blake et. al. 2014) convinced eBay to stop bidding on any AdWords (the
marketplace through which Google SEM is sold) for 65 of the 210 DMAs where eBay was
previously advertising. These DMAs are viewed as roughly independent markets around
metropolitan centers ranging from Boston to Los Angeles. The pre-treatment period corresponds
to the period April 1, 2012 to May 21, 2012, and the treatment period was the eight weeks
following (and including) May 22, 2012. To be sure, here, treatment means: SEM is off. For the
control DMAs, SEM is on throughout the pre and post treatment period.

###The Approach
I structure the data for analysis in alignment with Arkhangelsky et. al. (2021) and construct point estimates and 95% confidence intervals of the impact on revenue that paid SEM marketing has in percentage points.

###Conclusions
What is most surprising is that for each of our estimation methods, we derive positive estimates of $\tau$, our treatment effect.  The standard Diff-in-Diff (DID) stood just apart from the other two methods with an estimated treatment effect of .007, which equates to a 0.7 percentage point increase in sales at eBay when they quit paying for SEM. Our Synthetic Control (SC) method estimate closely resembled the Synthetic Diff-in-Diff (SDID) estimate at 0.012 and 0.011, respectively. Thus SC and SDID estimate a 1.1 and 1.2 percentage point increase in sales if eBay quits paying for SEM. 

What is perhaps most important is that the standard errors on each of our models' estimates are large enough that none of them are 'statistically significant'. Our confidence intervals are split between positive and negative values, so we can't rule out that the treatment effect was negative either. Ultimately, we can't be confident about whether or not the treatment helps or hurts sales, but it does seem likely that the magnitude of the effect is negligible. Considering the fact that eBay could utilize their SEM budget in other ways, these results indicate that they should reallocate those funds to other efforts. In 'Business Data Science' Matt Taddy makes an important note on this conclusion: these results are very likely driven by the fact that eBay is so well known that it appears in search results organically. A less known company might have very different results.
