## Research Question: Do publications negatively portray certain candidates more than other candidates?

### Literature Review

Our capstone project aims to measure bias in news media coverage for the candidates in the United States 2020 Democratic Presidential Primary. The Literature Review section focus on a selection of published literature and analyses that define political bias and identify ways of measuring and quantifying these biases. 

Sutter [1] suggests that journalism, the main transmission engine for ideas and information in society, is inherently subjective and often reflects the opinions of the journalist and/or news outlet. However, the evidence to prove the existence of bias is circumstantial, making the measurement and quantification of these biases is very difficult. Sutter notes that revenue is a controlling force for limiting or reducing bias in privately owned news media organizations. He argues that the inclusion of too much bias in reporting can adversely affect the readership and advertising revenue for the news organizations.

Like Sutter, Baron [2] submits that profit-maximizing, competitive pressures, consumer preferences, and the general economic and financial landscapes impact the role of bias in news media. Unlike Sutter, Baron theorizes that there are strong correlations between political biases and consumer expectations, operational costs, and the ideological alignment of the employed journalists. Baron’s findings show that several forces combine to ensure the presence and prevalence of unbalanced reporting.

Bernhardt [3] also suggests that profit-maximization may influence a news media outlet to cater to a more partisan audience by suppressing or doctoring some pertinent information in its news reporting. The model examines the undesirable “electoral mistakes” that are generated from the existence of media bias. Bernhardt cautions that the impact of media bias is more powerful and determinative than commonly presumed, since its effect cannot be nullified, even to a rational consumer.

Baum and Groeling [4] submits that the advent of internet media removed the professional editorial process from news content. The new "partisan" styled editorial system of internet news paired with the public's adoption of the internet produced a more fragmented audience. Baum and Groeling’s study found that left-skewed and right-skewed political biases exist in internet news media. This shift from bipartisan to partisan coverage has important implications for political discourse in America and may impact the decision making for many Americans.

Gentzkow and Shapiro [5] examine the accuracy and trust in media. The paper explains how different media outlets select, discuss and present facts in ways that tend to systematically favor one side of the political spectrum. These biases can be a result from a multitude of different media components. Supply-side bias persists when media management or labor are willing to sacrifice profits for political gain. Demand-side bias persists when consumers perceive biased media to be more informative or more enjoyable. Like Baum and Groeling, Gentzkow and Shapiro believe these differences can have large effects on voter behavior, public perception and political outcomes. However, it is very difficult to determine the measured impact of these biases. 

Stone [6] presents the counterintuitive thesis that bias can be more prevalent in certain competitive media markets than in some less competitive ones. It presents a formal proof that consumers can, for example, be less informed in some media duopolies than in some monopolies. Thus, one must guard against simplistic prescriptions on how to counter bias, since its correlations with market conditions can be contrary to intuition.

Sheth [7] proposes a model for measuring the ideological bias in news coverage by mainstream media outlets. Terms in the news articles are classified based on detected political affiliations: pro-conservative, anti-conservative, pro-liberal and anti-liberal. Once classified, the model detects the overall measurement of political bias in each article. Sheth’s initial findings are that media coverage is broadly anti-conservative. The model also concludes that the news outlets, regardless of political affiliations, are resoundingly negative and critical of the opposition instead of championing its respective candidates. The Sheth model findings align with the general public's perception of media bias. 

Lin, Bagrow and Lazer [8] propose a method of quantifying bias in both traditional news media and internet blogs. The method is primarily based on comparing the number of references to members of the US Congress, thus avoiding errors due to subjective criteria such as sentiment and degrees of bias. Lin, Bagrow and Lazer note that these methods to measure how bias vary over time. They also measure links between blog articles and how media outlets with different slants link to each other. The findings conclude that internet blogs are "more social", i.e. more influenced by the network of sites that they are connected to, and more "exogenous", meaning their coverage is more influenced by external factors such as election cycles.

Oconnor, Balasubramanyan, Routledge and Smith [9] sought to test how well twitter sentiment analysis correlates with consumer confidence polling data as well as presidential approval/election polling data.  The sentiment analysis model is based on a lexicon from OpinionFinder on a subset of twitter data relating to several political topics in 2008-2009 (jobs, Obama, Mccain ).  The sentiment score is a ratio of positive to negative words.  The sentiment data was extremely noisy, so smoothing averages to clean out some of the noise to determine correlation.  They found techniques like stemming caused dangerous misclassification over their lexicon (in particular stemming jobs to job) but that overall this did not substantially effect the aggregated scoring composites.  Results were mixed with the sentiment analysis doing well predicting the economic indicators, but not as well at predicting the presidential approval polls.      

Groceclose and Milyo [10] proposes a method to estimate the ADA scores for media outlets, which involves many functions that are similar to a multinomial logit. By comparing the citation patterns, they construct an ADA score that will simplified example. Since Groseclose and Milyo's measure of bias is restricted to citations of think tank and advocacy groups, this kind of miscategorization is inevitable. Groseclose and Milyo's discussion of the idea of bias assumes that if a reporter quotes a source, then the opinion expressed by that source is an accurate measure of the reporter's beliefs an assumption that most, if not all, reporters across the ideological spectrum would find utterly ridiculous. Their method is primarily based on comparing the liberal group and conservative group based on the average of score of legislators. They also measure links between new outlets media which compute the measure, by counting the times that a media outlet cites various think tanks and other policy groups. But sometimes can submit a false and negative result depending in different media sources.

### References

1. Sheth, Dev. "Measuring Ideological Bias in News Coverage of Political Events by Print Media Using Data Analytics." Rochester Institute of Technology , 2016, pp. 1-21.

2. Baron, D. P. (2004). Persistent media bias. Journal of Public Economics, 90 (2006), 1 - 36.  https://pdfs.semanticscholar.org/2abb/9660637a260e5342c3e2c00abb07ab903978.pdf

3. Bernhardt, D., Krasa, S., Polborn, M. (2008). Political polarization and the electoral effects of media bias. Journal of Public Economics, 92 (2008), 1092 - 1104. http://www.econ.uiuc.edu/~skrasa/media_bias_december_2007.pdf

4. Stone, D. (2011). Ideological media bias. Journal of Economic Behavior & Organization, 78 (2011), 256-271.

5. Gentzkow and Shapiro. Media Bias in the Marketplace: Theory. https://web.stanford.edu/~gentzkow/research/handbook.pdf   

6. Groseclose, T., Milyo, J. (2005). A measure of media bias. The Quarterly Journal of Economics, CXX (4), 1191-1237. 
http://itre.cis.upenn.edu/~myl/GrosecloseMilyo.pdf

7. Baum and Groeling (2008). New Media and the Polarization of American Political Discourse.
https://journalistsresource.org/wp-content/uploads/2012/03/News-Media-and-Polarization-Matt-Baum_Political-Communication-LK.pdf

8. Lin, Bagrow and Lazer (2011). More Voices Than Ever? Quantifying Media Bias in Networks. https://arxiv.org/pdf/1111.1227.pdf

9. B. O'Connor, R. Balasubramanyan, B.R. Routledge, and N.A. Smith. From Tweets to Polls: Linking Text Sentiment to Public Opinion Time Series.
https://homes.cs.washington.edu/~nasmith/papers/oconnor+balasubramanyan+routledge+smith.icwsm10.pdf

10. Sutter, D. (2012).Mechanisms of Liberal Bias in the News Media versus the Academy.http://www.independent.org/pdf/tir/tir_16_03_4_sutter.pdf
