# What is data science

## Why has data science become a popular role?

More and more data is being collected, hence the term Big data has been coined. This data is from social media, enterprise data, sensors and media.

At what stage of the data flow does the data scientist come in?

1. Data collection and storage
2. Data preparation (data scientist)*
3. Exploration and visualisation (data scientist)*
4. Experimentation and prediction (data scientist)*
5. Data storytelling and communication (data scientist)*

## Step 1:  Data collection

Data engineer collects data and creates SQL databases for data to be stored in.

## Step 2:  Data preparation

This stage is cleaning and transforming the data into a format that’s ready for analysis. Cleaning techniques such as removing duplicates, inconsistent data and normalisation are used.

Cleaning techniques such as removing duplicates, inconsistent data and normalisation are used.

Tidy data is a way of presenting a matrix of data, with observations on rows and variables as columns.

1. Remove duplicates or Unique ID
2. Homogeneity - same units etc.
3. Same data types
4. Missing values
    1. Impute - use a mean value
    2. Drop
    3. Keep

## Step 3: Exploration and visualisation

During this phase, data scientists explore the data to understand patterns, understand characteristics or spot anomalies. Statistics and visualisation plots are used to gain meaningful insights from the data.

### Step 3a: Exploration

Streaming through the data gives you little information. Descriptive statistics do better, but can be misleading; visualisation teaches us the most.

Anscombe's quartet is a group of datasets (x, y) that have the same mean, standard deviation, and regression line, but which are qualitatively different.

### Step 3b: Visualisations

Rules for plots:
    - Use colours intentially
    - Axes - make sure the axes are sensible. Not always 0, as you might want to see change.

Dashboard
    - A picture of several pictures. Individually, these pieces of information are useful. But together, they paint a much bigger picture

## Step 4: Experimentation and prediction

We run experiments and predictions on the data to get insights.

At this stage, the data scientist runs experiments and predictions on the data to get insights. The aim is to meet the project objective to predict future outcomes, classify data, or uncover hidden patterns. They can use A//B testing and/or machine learning -  where a model is trained on data to make predictions.

### Step 4a: Experimentation

Experiments help drive decisions and draw conclusions. Generally, they begin with a question and a hypothesis, then data collection, followed by a statistical test and its interpretation. This is where we might use A/B testing:

1. Picking a metric
    1. Our metric is click-through rate, the percent of people who click on a link after viewing the title.
2. Picking a sample size
    1. Next, we'll run the experiment until we reach a sample size large enough to be certain that results aren't due to random chance.
    2. The size depends on a "baseline metric" that helps gauge any changes. In our case, it's how often people click on a link to one of our blogs usually. If the rate is much larger or smaller than 50%, then we need a larger sample size. Click-rate is typically under 3%.
    3. The sample size depends on the sensitivity we want. A test's sensitivity tells us how small of a change in our metric we can detect. Larger sample sizes allow us to detect smaller changes. You might think that we want a high sensitivity, but we actually want to optimise for an amount that is meaningful for our question
3. We run our experiment until we reach the calculated size. Stopping the experiment before or after could lead to biassed results
    1. Once we reach the target size, we check our metric. We see some difference between the titles, but how do we know if it's meaningful? We check by performing a test of statistical significance. If they are significant, we can be reasonably sure that the difference is not due to random chance, but to an actual difference in preference.
4. Checking for significance.
    1. Once we reach the target size, we check our metric. We see some difference between the titles, but how do we know if it's meaningful? We check by performing a test of statistical significance. If they are significant, we can be reasonably sure that the difference is not due to random chance, but to an actual difference in preference.
    2. A statistically significant result means that your result is probably not due to chance given the statistical assumptions made.
    3. If it’s not significant, we can't conclude which option is better because the observed difference is likely due to random chance.
5. Finally, we interpret the results. In our case, we want to choose the better performing title

### Step 4b: Make models for prediction

Models attempt to represent a real-world process with statistics. At a high level, models define relationships between variables with equations. These definitions are based on statistical assumptions and historical data.

Predictive modelling is a subcategory of modelling used for prediction. By modelling a process, we can enter new inputs and see what outcome it outputs. Predictive models can be as simple as a linear equation with an x and y variable to a deep learning algorithm that is uninterpretable by humans.

Often when plotting time series, you can find patterns. Seasonality is when there are repeating patterns related to time such as months and weeks.Time series data is used in predictive modelling to predict metrics at future dates. We call this forecasting. We can build predictive models using time series data from the past years or decades to generate predictions. This uses a combination of statistical and machine learning methods.

Machine learning simply is teaching a machine to learn from data.

While Supervised Learning uses data with features and labels, Unsupervised Learning uses data with only features. Labels are what we want to predict, like the customer churning. Features are data that might help predict the label, such as profession or date of last purchase.

### Step 4c: Model evaluation

After training a model, how do we know if it's any good? It's always good practice not to allocate all of your historical data for training. Withheld data is called a test set and can be used to evaluate the goodness of the model. In our example, we could ask the model to predict whether a set of customers would churn, and then measure the accuracy of our prediction.

### Step 5. Data storytelling and communication

The final stage is communicating your insights effectively. The language must be clear, concise with compelling visuals for a non-technical audience.
