a={
"CD09":{"product_name":"9 Months","apy":34.9,"interest_rate":34.33},  
"CD12":{"product_name":"12 Months","apy":34.9,"interest_rate":34.33},
"CD24":{"product_name":"24 Months","apy":0.54,"interest_rate":34.33},
"CD36":{"product_name":"36 Months","apy":None,"interest_rate":34.33}
}


cd24={'apy':None,'interest_rate':34.33}

cd_rates=a.get('CD24',{})
int_cd24=cd24.get('interest_rate')
apy_cd24=cd24.get('apy')

intcore=cd_rates.get('interest_rate')
apycore=cd_rates.get('apy')
print(int_cd24)
print(apy_cd24)
print(intcore)
print(apycore)

interest=int_cd24 if int_cd24 else intcore
apy=apy_cd24 if apy_cd24 else apycore
print(f"interest is {interest}")
print(f"apy is {apy}")

a={"wedge":None}
are=a.get("wedge",{'a':2})
print(are)