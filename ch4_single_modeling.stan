// You can see also executable notebook https://github.com/ghmagazine/modelingbook/ch4_single_modeling.ipynb
data {
    int n;
    vector[n] x;
    vector[n] y;
}
parameters {
    real<lower=0, upper=1> a;
    real<lower=0> b;
    real<lower=0> sigma;
}
transformed parameters {
    vector<lower=0>[n] y_p;
    for(i in 1:n)
        y_p[i] = b*(x[i]^a) - x[i]; 
}
model {
    a ~ uniform(0, 1);
    b ~ uniform(0, 100);
    sigma ~ normal(0, 100);
    y ~ normal(y_p, sigma);
}