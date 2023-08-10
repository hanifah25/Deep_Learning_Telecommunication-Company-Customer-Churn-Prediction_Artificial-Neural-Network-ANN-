---

Data Science Project
Model Used - ANN (Artificial Neural Network)
Project - Deep Learning - Customer Churn Prediction

# Problem Statement 
A company wants to minimize the risk of a customer to stop using the product they offer. This process helps the company to predict which customers will stop (churn) from the given dataset.

# Objective
build an accurate churn prediction model using the given dataset, with the aim of minimizing the risk of a customer stopping using the product offered by the company.

# Overall analysis
* From the prediction results it can be concluded that the success of perfecting the model with accuracy on Sequential tune: 92% and Functional Tune: 93%
* The model can predict very well.
* Models can still be upgraded due to several factors such as: can add important Parameters to HyperParameter Tuning so that it can produce more optimal predictions.

# Conclusion
* It can be seen from the EDA above that the average customer transaction value tends to increase over time, from 2015 to 2017. This indicates that customers are becoming more active in making transactions and may be more loyal to the business. This can be a positive signal for a business to retain existing customers and attract new ones by offering attractive services or products.
* The majority of customers give "dissatisfied" or "neutral" feedback on the company's services (poor quality, too many ads, etc.). This needs to be considered by the company to improve service quality in order to increase customer satisfaction.
* In this case it is recommended to focus on customer satisfaction: To maintain customer satisfaction, companies need to ensure that the products and services offered are in accordance with customer needs and expectations. In conditions where the number of customer churn and non-churn is balanced, companies still need to pay attention to product or service quality, ensure customer retention, increase customer satisfaction, and increase customer loyalty to maintain healthy business growth.

---

## Dataset Description

Dataset name: `churn.csv`

| Column | Description |
| --- | --- |
| `user_id` | ID of a customer |
| `age` | Age of a customer |
| `gender` | Gender of a customer |
| `region_category` | Region that a customer belongs to |
| `membership_category` | Category of the membership that a customer is using |
| `joining_date` | Date when a customer became a member |
| `joined_through referral` | Whether a customer joined using any referral code or ID |
| `preferred_offer types` | Type of offer that a customer prefers |
| `medium_of operation` | Medium of operation that a customer uses for transactions |
| `internet_option` | Type of internet service a customer uses |
| `last_visit_time` | The last time a customer visited the website |
| `days_since_last_login` | Number of days since a customer last logged into the website |
| `avg_time_spent` | Average time spent by a customer on the website |
| `avg_transaction_value` | Average transaction value of a customer |
| `avg_frequency_login_days` | Number of times a customer has logged in to the website |
| `points_in_wallet` | Points awarded to a customer on each transaction |
| `used_special_discount` | Whether a customer uses special discounts offered |
| `offer_application_preference` | Whether a customer prefers offers |
| `past_complaint` | Whether a customer has raised any complaints |
| `complaint_status` | Whether the complaints raised by a customer was resolved |
| `feedback` | Feedback provided by a customer |
| `churn_risk_score` | Churn score <br><br> `0` : Not churn <br> `1` : Churn |

