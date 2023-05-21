{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5b52e08a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f91acfa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_csv(\"loan_data_set.csv.zip\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "152a4244",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0         NaN             360.0   \n",
       "1             4583             1508.0       128.0             360.0   \n",
       "2             3000                0.0        66.0             360.0   \n",
       "3             2583             2358.0       120.0             360.0   \n",
       "4             6000                0.0       141.0             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  \n",
       "0             1.0         Urban           Y  \n",
       "1             1.0         Rural           N  \n",
       "2             1.0         Urban           Y  \n",
       "3             1.0         Urban           Y  \n",
       "4             1.0         Urban           Y  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "59aa0c5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(614, 13)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e30c8e32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 614 entries, 0 to 613\n",
      "Data columns (total 13 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Loan_ID            614 non-null    object \n",
      " 1   Gender             601 non-null    object \n",
      " 2   Married            611 non-null    object \n",
      " 3   Dependents         599 non-null    object \n",
      " 4   Education          614 non-null    object \n",
      " 5   Self_Employed      582 non-null    object \n",
      " 6   ApplicantIncome    614 non-null    int64  \n",
      " 7   CoapplicantIncome  614 non-null    float64\n",
      " 8   LoanAmount         592 non-null    float64\n",
      " 9   Loan_Amount_Term   600 non-null    float64\n",
      " 10  Credit_History     564 non-null    float64\n",
      " 11  Property_Area      614 non-null    object \n",
      " 12  Loan_Status        614 non-null    object \n",
      "dtypes: float64(4), int64(1), object(8)\n",
      "memory usage: 62.5+ KB\n"
     ]
    }
   ],
   "source": [
    "dataset.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2142b6c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>614.000000</td>\n",
       "      <td>614.000000</td>\n",
       "      <td>592.000000</td>\n",
       "      <td>600.00000</td>\n",
       "      <td>564.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5403.459283</td>\n",
       "      <td>1621.245798</td>\n",
       "      <td>146.412162</td>\n",
       "      <td>342.00000</td>\n",
       "      <td>0.842199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6109.041673</td>\n",
       "      <td>2926.248369</td>\n",
       "      <td>85.587325</td>\n",
       "      <td>65.12041</td>\n",
       "      <td>0.364878</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>150.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>12.00000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2877.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3812.500000</td>\n",
       "      <td>1188.500000</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>5795.000000</td>\n",
       "      <td>2297.250000</td>\n",
       "      <td>168.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>81000.000000</td>\n",
       "      <td>41667.000000</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>480.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "count       614.000000         614.000000  592.000000         600.00000   \n",
       "mean       5403.459283        1621.245798  146.412162         342.00000   \n",
       "std        6109.041673        2926.248369   85.587325          65.12041   \n",
       "min         150.000000           0.000000    9.000000          12.00000   \n",
       "25%        2877.500000           0.000000  100.000000         360.00000   \n",
       "50%        3812.500000        1188.500000  128.000000         360.00000   \n",
       "75%        5795.000000        2297.250000  168.000000         360.00000   \n",
       "max       81000.000000       41667.000000  700.000000         480.00000   \n",
       "\n",
       "       Credit_History  \n",
       "count      564.000000  \n",
       "mean         0.842199  \n",
       "std          0.364878  \n",
       "min          0.000000  \n",
       "25%          1.000000  \n",
       "50%          1.000000  \n",
       "75%          1.000000  \n",
       "max          1.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9d1812df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Loan_Status</th>\n",
       "      <th>N</th>\n",
       "      <th>Y</th>\n",
       "      <th>All</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit_History</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0.0</th>\n",
       "      <td>82</td>\n",
       "      <td>7</td>\n",
       "      <td>89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1.0</th>\n",
       "      <td>97</td>\n",
       "      <td>378</td>\n",
       "      <td>475</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>All</th>\n",
       "      <td>179</td>\n",
       "      <td>385</td>\n",
       "      <td>564</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Loan_Status       N    Y  All\n",
       "Credit_History               \n",
       "0.0              82    7   89\n",
       "1.0              97  378  475\n",
       "All             179  385  564"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(dataset['Credit_History'],dataset['Loan_Status'], margins=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "163de5fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Ly8vkZqaKpqampxqLl68KBYuXCh8fX2Fr6+vWLhwoTAajU41jY2NIiUlRXh5eYmAgACxbNky0dPTM+BtYdAhUi4GHSLlcmX/rRJCCPfOKbmPK7d5J6Kbi81mQ1FREebOnctjdIgUxpX9N+91RURERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENEimO321FWVobDhw+jrKwMdrvd3S0RkZsw6BCRohQUFCAiIgKJiYnIz89HYmIiIiIiUFBQ4O7WiMgNGHSISDEKCgqwYMECREdHo7y8HDt37kR5eTmio6OxYMEChh2iYUglhBDubsJdzGYzJEmCyWSCn5+fu9shokGw2+2IiIhAdHQ09u7dC7vdjqKiIsydOxcajQbp6emor6/H6dOnodFo3N0uEQ2CK/tvzugQkSKUl5fjzJkzeP7556FWO3+1qdVqrF69Gg0NDSgvL3dTh0TkDgw6RKQILS0tAICoqKhrLu8b76sjouGBQYeIFCEkJAQAUF9ff83lfeN9dUQ0PDDoEJEiTJs2DWFhYcjNzYXD4XBa5nA4kJeXh/DwcEybNs1NHRKRO7gUdNauXQuVSuX0T6/Xy8uFEFi7di1CQ0Ph5eWFGTNm4Pjx407rsFgsWL58OQIDA+Hj44N58+bh7NmzTjVGoxGZmZmQJAmSJCEzMxPt7e1ONU1NTUhLS4OPjw8CAwOxYsUKWK1WFzefiJRCo9Fg8+bNKCwsRHp6Oqqrq9Hd3Y3q6mqkp6ejsLAQmzZt4oHIRMOMyzM63//+99HS0iL/O3bsmLxsw4YNyM/Px5YtW3D06FHo9XokJiaio6NDrsnKysKePXtgMBhQUVGBS5cuITU11emCXhkZGairq0NxcTGKi4tRV1eHzMxMebndbkdKSgo6OztRUVEBg8GA3bt3Iycn53rfByJSgPnz52PXrl04duwYpk+fjocffhjTp09HfX09du3ahfnz57u7RSL6rgkXrFmzRtx9993XXOZwOIRerxfr16+Xx3p6eoQkSWLr1q1CCCHa29uF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Nzc7vd7MmTPF6tWrv/6NIiIhhBAe7otYROROp06dwpEjR1BQUAAA8PDwwI9//GP8/ve/x6xZs+S6uLg4+e+AgABERkbik08+kcc8PDycZjXuuusu3Hrrrfjkk09w7733fmMPn3zyCSwWC2bOnPm1Nbt27cKvfvUrfPbZZ7h06RJ6e3v73Y08LCwMvr6+8uOQkBC0tbX9m3fg2iZOnOi0HgBoa2vD6NGjUVdXh8WLF3/ttnh4eCA2NlYeGzlyZL/3y9vbG2PHjpUfBwcHIywsDLfccovTWF//H330EYQQuPPOO51ez2KxYOTIkde1jUTDCYMO0TD15ptvore3F7fddps8JoSAVquF0Wj8xueqVKpvfPx1Y1fz8vL6xuXV1dV46KGHsG7dOiQnJ0OSJBgMBmzevNmpTqvV9ntth8Pxb1//Wq5cV9829K3rm/oVX3M3HSGE03txrV6/qX+HwwGNRoPa2lpoNBqnuivDERFdG4/RIRqGent78cc//hGbN29GXV2d/O8f//gHxowZg7fffluura6ulv82Go349NNPcddddzmt68MPP5Qfnzp1Cu3t7U41X2fcuHHw8vLC+++/f83lH3zwAcaMGYMXXngBkydPxrhx49DY2Ojy9np6ejod3Hu9Jk6c+LW9TpgwAb29vaipqZHHLl68iE8//RTjx4+/7tecNGkS7HY72traEBER4fRPr9df93qJhgvO6BANQ4WFhTAajXj88cchSZLTsgULFuDNN9+UD/j9xS9+gZEjRyI4OBgvvPACAgMDnc6a0mq1WL58OX79619Dq9Vi2bJlmDJlyr/92QoARowYgWeffRarVq2Cp6cn7rvvPpw/fx7Hjx/H448/joiICDQ1NcFgMOAHP/gB9u3bhz179ri8vWFhYaipqcGZM2dwyy23ICAgwOV1AMCaNWswc+ZMjB07Fg899BB6e3uxf/9+rFq1CuPGjcMDDzyAxYsXY9u2bfD19cVzzz2H2267DQ888MB1vR4A3HnnnVi4cCEeeeQRbN68GZMmTcKFCxfw97//HdHR0Zg7d+51r5toOOCMDtEw9Oabb2LWrFn9Qg4A/Od//ifq6urw0UcfAQDWr1+Pp556CjExMWhpacG7774LT09Pud7b2xvPPvssMjIyEBcXBy8vLxgMhgH38uKLLyInJwc///nPMX78ePz4xz+Wj0954IEH8PTTT2PZsmW45557UFlZiRdffNHl7V25ciU0Gg0mTJiA733ve9d9vaAZM2bgr3/9K959913cc889uP/++51mcLZv346YmBikpqYiLi4OQggUFRX1+2nKVdu3b8cjjzyCnJwcREZGYt68eaipqfnGs8eI6DKV+LofloloWDt06BASEhJgNBq/9gJ/O3bsQFZWFtrb27/T3oiIBoozOkRERKRYDDpERESkWPzpioiIiBSLMzpERESkWAw6REREpFgMOkRERKRYDDpERESkWAw6REREpFgMOkRERKRYDDpERESkWAw6REREpFgMOkRERKRY/x8hzaEqIygOsQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset.boxplot(column='ApplicantIncome')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d32bb2a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['ApplicantIncome'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3553209b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'ApplicantIncome'}, xlabel='Education'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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ZbVlW3l7e0OhUCAvLw8qlcpsHqY2U3xr61VRUdHme/pYmv7CZQDni4kXXngB//u//4u+ffuioqICzz77bJuW0RbWrE9bt7upSDH1jLWmtrYWW7ZswcKFC/Hiiy9K7TqdDmfOnLFuJS7g5eWF5uZmnD59WlYsif9/+47777//iudNdDk89EbURiUlJQD++4MxZMgQnDt3DpmZmbK4jz76SBpv8vTTT+P48ePIyMjA+++/jy+//BJvvPFGq8tZv369bPjTTz8FcOn7Hg0ZMgT79+/HDz/8YJaLQqHA4MGDAfy3MGjrX9YREREoLS3F/v37Ze0XXsl1OW3NzfTj/fPPP8vivvzyS4vzvty2iomJgRACZWVl6NOnj9krNDQUANC3b1+0a9fObH4FBQVWHa757rvvZIWl0WjEZ599hjvvvFPWE9OuXTtMnToVH374IdLS0tCrVy8MGDCgzcu5HGvWp63bvX///tBoNFizZg2EEK0uV6FQQAhhVpS+99570tWdJtZ8Fk370ieffCJr37RpE+rr62X7GtE1Z7vTo4huPKYTWz/44APpSpwtW7aISZMmCQCyk2NNV725ubmJtLQ0kZOTIxYuXCiUSqXsqrd3333X7GTkGTNmCKVSKTvB+VJXcg0fPlyWp6Wr3rRarXjnnXfEN998I2bNmiUUCoXsiiTTtMHBweKbb74Re/bsMTuJ90JlZWWyq962bdsmEhISRJcuXcyuIoqIiBB333232TysyW3o0KHCw8NDvPvuuyI7O1u88MILomvXrlZd9Xbxtpo6dapwcXERc+fOFV999ZXYvn27WL9+vXjmmWdkJ+i/9NJL0lViWVlZ4t13371mV72lp6ebxZ84cUI4OTkJAOK999677PyF+O/J3DNnzpQ+nxe+LryCsa3r09zcLIKDg0Xnzp3Fp59+KrZt2yamTp0qAgMDW73qDYB46KGHxIYNG8T27dvFO++8I5599lkpJjw8XHh6eop3331X5OTkiJdeekn4+fmJ2267TfaZ/f333wUAMWbMGJGXlyf27Nkj/vzzTyGE5avelEqlWLRokcjJyRGpqamiffv2rV71NnLkSLNtFxER0ab3kehiLJSILtDaVW8ajUb06tVLpKWlyb6QhRCiqqpKPP3008LPz084OTmJLl26iPnz50txP//8s1Cr1bIfCCHOX6rfu3dvERAQIKqr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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset.boxplot(column='ApplicantIncome' , by= 'Education')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6358c6c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAGdCAYAAAA44ojeAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA7JklEQVR4nO3dfXhU9Z3//9ckmYwkJhECZJISSTRBqglKoQWhEO4SCqKkXBRXije7dAtFsDFBFNxW6LpBUaKtqVgLKy2u0i0E6tLAJlYMYSMtxKVLEDXSAAIJQYyZ3JEMk/P9g1/OzyGoDFDOIXk+rouLzOe8Z+Z9uK7hvPI5nznHYRiGIQAAABsJsroBAACAcxFQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7YRY3cDFaG9v1/HjxxURESGHw2F1OwAA4AIYhqGGhgbFxcUpKOjL50iuyoBy/PhxxcfHW90GAAC4CB9//LH69ev3pTVXZUCJiIiQdHYHIyMjLe4GwOXk9XpVVFSkjIwMOZ1Oq9sBcBl5PB7Fx8ebx/Evc1UGlI7TOpGRkQQUoIvxer0KCwtTZGQkAQXooi5keQaLZAEAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUADYhs/nU0lJiXbs2KGSkhL5fD6rWwJgkYACSkJCghwOR6c/Dz74oKSzNwFaunSp4uLi1KNHD40ZM0b79+/3e43W1lYtWLBAvXv3Vnh4uO666y4dPXr08u0RgKtSQUGBkpKSlJ6erry8PKWnpyspKUkFBQVWtwbAAgEFlN27d6u6utr8U1xcLEn63ve+J0lasWKF8vLylJ+fr927d8vtdis9PV0NDQ3ma2RlZWnTpk1av369du7cqcbGRk2ZMoXflIBurKCgQNOnT1dqaqpKS0v1+uuvq7S0VKmpqZo+fTohBeiOjEvw4x//2LjxxhuN9vZ2o7293XC73cZTTz1lbj99+rQRFRVlvPTSS4ZhGMZnn31mOJ1OY/369WbNsWPHjKCgIGPbtm0X/L719fWGJKO+vv5S2gdgA2fOnDESEhKMO++80/D5fEZbW5uxefNmo62tzfD5fMadd95pJCYmGmfOnLG6VQCXKJDj90XfLLCtrU2vvvqqsrOz5XA49Le//U01NTXKyMgwa1wul9LS0lRWVqY5c+aovLxcXq/XryYuLk4pKSkqKyvTxIkTz/tera2tam1tNR97PB5JZ28q5vV6L3YXANhASUmJDh06pHXr1snn85mf6Y6/H3nkEY0ePVrbt29XWlqala0CuESBHLMvOqBs3rxZn332mR544AFJUk1NjSQpJibGry4mJkaHDx82a0JDQ9WzZ89ONR3PP5/ly5dr2bJlncaLiooUFhZ2sbsAwAZ27NghSTp69KhOnTpljnecQm5paZEkbd26VU1NTVe+QQCXTXNz8wXXXnRAWbNmjSZNmqS4uDi/8XNvoWwYxlfeVvmrahYvXqzs7GzzscfjUXx8vDIyMhQZGXkR3QOwi/DwcOXl5alfv34aNmyYvF6viouLlZ6eLqfTqV27dkmSJk2axAwKcJXrOANyIS4qoBw+fFhvvvmm38I1t9st6ewsSWxsrDleW1trzqq43W61tbWprq7ObxaltrZWI0aM+ML3c7lccrlcncadTqecTufF7AIAmxg7dqwSEhK0YsUKbd682Rx3Op0KDg7WM888o8TERI0dO1bBwcHWNQrgkgVyzL6o66C88sor6tu3r+644w5zLDExUW6325yWlc6uUykpKTHDx5AhQ+R0Ov1qqqurVVFR8aUBBUDXFRwcrJUrV2rLli3KzMzUrl271NLSol27dikzM1NbtmzRs88+SzgBupmAZ1Da29v1yiuv6P7771dIyP//dIfDoaysLOXm5io5OVnJycnKzc1VWFiYZs6cKUmKiorS7NmzlZOTo+joaPXq1UsLFy5UamqqJkyYcPn2CsBVZdq0adqwYYNycnI0evRoczwxMVEbNmzQtGnTLOwOgBUCDihvvvmmjhw5on/6p3/qtG3RokVqaWnRvHnzVFdXp2HDhqmoqEgRERFmzXPPPaeQkBDNmDFDLS0tGj9+vNauXctvR0A3N23aNE2dOlXbt2/X1q1bNWnSJE7rAN2YwzAMw+omAuXxeBQVFaX6+noWyQJdjNfrVWFhoSZPnswaM6CLCeT4zb14AACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQANiGz+dTSUmJduzYoZKSEvl8PqtbAmARAgoAWygoKFBSUpLS09OVl5en9PR0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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset.boxplot(column='LoanAmount')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a875fc15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['LoanAmount'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4fdc8c68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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sd57771klzbq/fGPf9TWrVtVUFCg/fv36+6779a9996rn//858kubcRK+U+SXbt2rZ5++mkdOnRIV199dbLLwV/19vbq5MmT+stf/qJf/vKX+tnPfqampiZCSpKdOnVKRUVFOnDggGbNmiVJKikp0XXXXae6urrkFodBzp07p8985jNav369Kisrk13OqDZmzBgVFRWpubk5NnbvvffqyJEjeumll5JY2ciV0ntQ1q1bp7179+rgwYOEE2PGjBmjz372syoqKlJNTY1mzZqlH/3oR8kua9RrbW1Ve3u7Zs+erYyMDGVkZKipqUn/+Z//qYyMDPX19SW7RHzI+PHjNXPmTL355pvJLmXUmzp16qA/sD7/+c/r5MmTSapo5EvJk2Qdx9G6deu0e/duPf/888rPz092SbgIx3EUiUSSXcaoN3/+/EHvCrnzzjt1zTXX6IEHHlB6enqSKsNQIpGI/vCHP+hLX/pSsksZ9ebOnTvo4yzeeOONYX3BLYYnJQPK2rVr1djYqF//+tfKyspSOByWJE2cOFHjxo1LcnX413/9Vy1atEh5eXnq7u7Wrl279Pzzzw969xU+eVlZWYPO1Ro/frxycnI4h8uA+++/X0uXLtW0adPU3t6uH/zgB+rq6tKqVauSXdqo993vflfFxcWqrq7W8uXL9corr2jbtm3atm1bsksbsVIyoGzdulXSB8fOP2z79u361re+9ckXhDj/+7//q5UrV+rMmTOaOHGirr32Wj377LMqKytLdmmAae+8846+8Y1v6E9/+pP+9m//Vv/wD/+gl19+mb/SDbjhhhu0e/duVVVV6aGHHlJ+fr7q6up0++23J7u0ESvlT5IFAAAjT0qfJAsAAEYmAgoAADCHgAIAAMwhoAAAAHMIKAAAwBwCCgAAMIeAAgAAzCGgAAAAcwgoAADAHAIKAAAwh4ACAADMIaAAAABz/h/X82G0mk7aNAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['LoanAmount_log']=np.log(dataset['LoanAmount'])\n",
    "dataset['LoanAmount_log'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "96bd4917",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender               13\n",
       "Married               3\n",
       "Dependents           15\n",
       "Education             0\n",
       "Self_Employed        32\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount           22\n",
       "Loan_Amount_Term     14\n",
       "Credit_History       50\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "LoanAmount_log       22\n",
       "dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "52c3471f",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5f42b392",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Married'].fillna(dataset['Married'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ba2f5186",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Dependents'].fillna(dataset['Dependents'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e12217d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3617ec32",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset.LoanAmount = dataset.LoanAmount.fillna(dataset.LoanAmount.mean())\n",
    "dataset.LoanAmount_log = dataset.LoanAmount_log.fillna(dataset.LoanAmount_log.mean())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9f51e73e",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5e2202b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c01be167",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID              0\n",
       "Gender               0\n",
       "Married              0\n",
       "Dependents           0\n",
       "Education            0\n",
       "Self_Employed        0\n",
       "ApplicantIncome      0\n",
       "CoapplicantIncome    0\n",
       "LoanAmount           0\n",
       "Loan_Amount_Term     0\n",
       "Credit_History       0\n",
       "Property_Area        0\n",
       "Loan_Status          0\n",
       "LoanAmount_log       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "d7bf3253",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['TotalIncome']= dataset['ApplicantIncome'] + dataset['CoapplicantIncome']\n",
    "dataset['TotalIncome_log']= np.log(dataset['TotalIncome'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "fb948ae1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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I55XU1OjCy64QMnJyRo5cqSWLFnSTxX3Tl/6c9setrS0qKioSKeddppSUlI0btw41dXVHfEct+yf1Pv+BvL+vf7667r66qsVCATk8Xi0bt26qPuNMQoGgwoEAkpJSdGECRO0devWo667evVqnX322fL5fDr77LO1du3aGHVwZLHob/ny5d3u5zfffBPDTrp3tP7WrFmjiRMn6qSTTpLH49GWLVt6tK5b9q8v/Tm1f4Qbh9XV1WnXrl2RW+cbFV577bVHPG/btm1R5+Xk5PRHub22aNEiLVmyRBUVFfr4449VWlqqxx9/XIsXLz7sOQ0NDbrqqqv0ox/9SPX19XrwwQf161//WqtXr+7HynumL/11csse3nnnnaqurtazzz6rDz74QAUFBbriiiu0c+fObue7af+k3vfXaSDu3/79+3XeeeepoqKi2/tLS0tVVlamiooK1dXVye/3Kz8/Xy0tLYdd86233tL111+vqVOn6v3339fUqVN13XXX6Z133olVG4cVi/6kb9/d97t7uWvXLiUnJ8eihSM6Wn/79+9XXl6eFi5c2OM13bR/felPcmj/YvrJVTD33nuvOf30001HR0e397/66qtGkmlqaurfwvpo0qRJ5vbbb48amzJlirn55psPe87s2bPNqFGjosamT59uLr744pjUeCz60p+b9rC1tdUkJiaaF154IWr8vPPOM3Pnzu32HDftX1/6c8v+STJr166NHHd0dBi/328WLlwYGfvmm2/M0KFDzZIlSw67znXXXWd+8pOfRI1NnDjR3HDDDY7X3BtO9bds2TIzdOjQGFbaN4f2910NDQ1Gkqmvrz/qOm7Zv+/qTX9O7R9XbmKora1NK1eu1O23337UD/gcPXq0MjMzdfnll+vVV1/tpwp779JLL9Xf/vY3ffLJJ5Kk999/Xxs3btRVV1112HPeeustFRQURI1NnDhRmzZtUjgcjmm9vdWX/jq5YQ8PHjyo9vb2Lv8KSklJ0caNG7s9x03715f+Orlh/76roaFBjY2NUXvj8/k0fvx41dbWHva8w+3nkc6Jh772J0n79u3TaaedplNPPVWTJ09WfX19rMvtN27Zv2PhxP4RbmJo3bp1+vrrr3Xrrbcedk5mZqaWLl2q1atXa82aNTrzzDN1+eWX6/XXX++/QnvhgQce0I033qhRo0bJ6/Vq9OjRKioq0o033njYcxobG7t8IGpGRoYOHjyoL7/8MtYl90pf+nPTHqalpemSSy7Ro48+qi+++ELt7e1auXKl3nnnHe3atavbc9y0f33pz037912dHzzc3d4c+qHEh57X23Pioa/9jRo1SsuXL9fzzz+vP/3pT0pOTlZeXp7+9a9/xbTe/uKW/esrp/Yvbh+/MBg888wzuvLKKxUIBA4758wzz9SZZ54ZOb7kkku0Y8cO/e53v9Nll13WH2X2yqpVq7Ry5UpVVlbqnHPO0ZYtW1RUVKRAIKBp06Yd9rxDr1yZ/31j7KNd0epvfenPbXv47LPP6vbbb9cpp5yixMREnX/++SosLNR777132HPcsn9S7/tz2/4dqru9Odq+9OWceOltrRdffLEuvvjiyHFeXp7OP/98LV68WH/4wx9iVmd/ctP+9ZZT+8eVmxjZvn27XnnlFd155529Pvfiiy8esP/KuP/++1VcXKwbbrhB5557rqZOnar77rtPCxYsOOw5fr+/y78qdu/eraSkJA0bNizWJfdKX/rrzkDew9NPP101NTXat2+fduzYoXfffVfhcFjZ2dndznfT/km97687A3n/Ovn9fknqdm8O/Zf9oef19px46Gt/h0pISNCFF1444Pezp9yyf07p6/4RbmJk2bJlOvnkkzVp0qRen1tfX6/MzMwYVHXsWltblZAQ/bRJTEw84kulL7nkksirxjpVVVVpzJgx8nq9Mamzr/rSX3cG8h52Ou6445SZmammpiZt2LBB11xzTbfz3LR/39XT/rrjhv3Lzs6W3++P2pu2tjbV1NRo3Lhxhz3vcPt5pHPioa/9HcoYoy1btgz4/ewpt+yfU/q8f8f8K8noor293QwfPtw88MADXe4rLi42U6dOjRw/8cQTZu3ateaTTz4xH374oSkuLjaSzOrVq/uz5B6bNm2aOeWUU8wLL7xgGhoazJo1a8xJJ51kZs+eHZlzaI+fffaZSU1NNffdd5/56KOPzDPPPGO8Xq/5y1/+Eo8Wjqgv/bltD19++WXz0ksvmc8++8xUVVWZ8847z1x00UWmra3NGOPu/TOm9/0N5P1raWkx9fX1pr6+3kgyZWVlpr6+3mzfvt0YY8zChQvN0KFDzZo1a8wHH3xgbrzxRpOZmWmam5sja0ydOtUUFxdHjt98802TmJhoFi5caD7++GOzcOFCk5SUZN5++20r+gsGg+bll182n376qamvrze33XabSUpKMu+8886A62/Pnj2mvr7erF+/3kgyzz33nKmvrze7du06bH9u2r++9OfU/hFuYmDDhg1Gktm2bVuX+6ZNm2bGjx8fOV60aJE5/fTTTXJysjnhhBPMpZdeatavX9+P1fZOc3Ozuffee83w4cNNcnKyGTlypJk7d64JhUKROYf2aIwxr732mhk9erQZMmSIGTFihHnqqaf6ufKe6Ut/btvDVatWmZEjR5ohQ4YYv99vZs6cab7++uvI/W7eP2N6399A3r/Ol6kfeps2bZox5tuXSz/yyCPG7/cbn89nLrvsMvPBBx9ErTF+/PjI/E5//vOfzZlnnmm8Xq8ZNWpU3IJcLPorKioyw4cPN0OGDDHf+973TEFBgamtre3Hrv7P0fpbtmxZt/c/8sgjkTXcvH996c+p/fMY87+/GQgAAGABfucGAABYhXADAACsQrgBAABWIdwAAACrEG4AAIBVCDcAAMAqhBsAAGAVwg0AALAK4QYAAFiFcAMAAKxCuAEAAFYh3AAAAKv8f3Dxfjk0CYsgAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['TotalIncome_log'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "a4d18ab8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "      <th>LoanAmount_log</th>\n",
       "      <th>TotalIncome</th>\n",
       "      <th>TotalIncome_log</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>146.412162</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.857444</td>\n",
       "      <td>5849.0</td>\n",
       "      <td>8.674026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "      <td>4.852030</td>\n",
       "      <td>6091.0</td>\n",
       "      <td>8.714568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.189655</td>\n",
       "      <td>3000.0</td>\n",
       "      <td>8.006368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.787492</td>\n",
       "      <td>4941.0</td>\n",
       "      <td>8.505323</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.948760</td>\n",
       "      <td>6000.0</td>\n",
       "      <td>8.699515</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0  146.412162             360.0   \n",
       "1             4583             1508.0  128.000000             360.0   \n",
       "2             3000                0.0   66.000000             360.0   \n",
       "3             2583             2358.0  120.000000             360.0   \n",
       "4             6000                0.0  141.000000             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  LoanAmount_log  TotalIncome  \\\n",
       "0             1.0         Urban           Y        4.857444       5849.0   \n",
       "1             1.0         Rural           N        4.852030       6091.0   \n",
       "2             1.0         Urban           Y        4.189655       3000.0   \n",
       "3             1.0         Urban           Y        4.787492       4941.0   \n",
       "4             1.0         Urban           Y        4.948760       6000.0   \n",
       "\n",
       "   TotalIncome_log  \n",
       "0         8.674026  \n",
       "1         8.714568  \n",
       "2         8.006368  \n",
       "3         8.505323  \n",
       "4         8.699515  "
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "72d5e839",
   "metadata": {},
   "outputs": [],
   "source": [
    "X= dataset.iloc[:,np.r_[1:5,9:11,13:15]].values\n",
    "y= dataset.iloc[:,12].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "62595659",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Male', 'No', '0', ..., 1.0, 4.857444178729353, 5849.0],\n",
       "       ['Male', 'Yes', '1', ..., 1.0, 4.852030263919617, 6091.0],\n",
       "       ['Male', 'Yes', '0', ..., 1.0, 4.189654742026425, 3000.0],\n",
       "       ...,\n",
       "       ['Male', 'Yes', '1', ..., 1.0, 5.53338948872752, 8312.0],\n",
       "       ['Male', 'Yes', '2', ..., 1.0, 5.231108616854587, 7583.0],\n",
       "       ['Female', 'No', '0', ..., 0.0, 4.890349128221754, 4583.0]],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "643e692e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "0ae58eec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Male' 'Yes' '0' ... 1.0 4.875197323201151 5858.0]\n",
      " ['Male' 'No' '1' ... 1.0 5.278114659230517 11250.0]\n",
      " ['Male' 'Yes' '0' ... 0.0 5.003946305945459 5681.0]\n",
      " ...\n",
      " ['Male' 'Yes' '3+' ... 1.0 5.298317366548036 8334.0]\n",
      " ['Male' 'Yes' '0' ... 1.0 5.075173815233827 6033.0]\n",
      " ['Female' 'Yes' '0' ... 1.0 5.204006687076795 6486.0]]\n"
     ]
    }
   ],
   "source": [
    "print(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "b664f2ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "labelencoder_X = LabelEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "56f4e1e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0, 5):\n",
    "    X_train[:,i]= labelencoder_X.fit_transform(X_train[:,i])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "5c1234bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train[:,7]= labelencoder_X.fit_transform(X_train[:,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "844e9729",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 1, 0, ..., 1.0, 4.875197323201151, 267],\n",
       "       [1, 0, 1, ..., 1.0, 5.278114659230517, 407],\n",
       "       [1, 1, 0, ..., 0.0, 5.003946305945459, 249],\n",
       "       ...,\n",
       "       [1, 1, 3, ..., 1.0, 5.298317366548036, 363],\n",
       "       [1, 1, 0, ..., 1.0, 5.075173815233827, 273],\n",
       "       [0, 1, 0, ..., 1.0, 5.204006687076795, 301]], dtype=object)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "34bd7971",
   "metadata": {},
   "outputs": [],
   "source": [
    "labelencoder_y=LabelEncoder()\n",
    "y_train= labelencoder_y.fit_transform(y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "a1797f29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,\n",
       "       0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,\n",
       "       1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0,\n",
       "       1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0,\n",
       "       1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,\n",
       "       0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1,\n",
       "       0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1,\n",
       "       0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1,\n",
       "       1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0,\n",
       "       1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,\n",
       "       1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1,\n",
       "       1, 1, 1, 0, 1, 0, 1])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8447d0bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0, 5):\n",
    "    X_test[:,i]= labelencoder_X.fit_transform(X_test[:,i])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "eb877464",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test[:,7]= labelencoder_X.fit_transform(X_test[:,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "728f854e",
   "metadata": {},
   "outputs": [],
   "source": [
    "labelencoder_y=LabelEncoder()\n",
    "y_test= labelencoder_y.fit_transform(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "349fe325",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 0, 0, 5, 1.0, 4.430816798843313, 85],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.718498871295094, 28],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.780743515792329, 104],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.700480365792417, 80],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.574710978503383, 22],\n",
       "       [1, 1, 0, 1, 3, 0.0, 5.10594547390058, 70],\n",
       "       [1, 1, 3, 0, 3, 1.0, 5.056245805348308, 77],\n",
       "       [1, 0, 0, 0, 5, 1.0, 6.003887067106539, 114],\n",
       "       [1, 0, 0, 0, 5, 0.0, 4.820281565605037, 53],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.852030263919617, 55],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.430816798843313, 4],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.553876891600541, 2],\n",
       "       [0, 0, 0, 0, 5, 1.0, 5.634789603169249, 96],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.4638318050256105, 97],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.564348191467836, 117],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.204692619390966, 22],\n",
       "       [1, 0, 1, 1, 5, 1.0, 5.247024072160486, 32],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.882801922586371, 25],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.532599493153256, 1],\n",
       "       [1, 1, 0, 1, 5, 0.0, 5.198497031265826, 44],\n",
       "       [0, 1, 0, 0, 5, 0.0, 4.787491742782046, 71],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.962844630259907, 43],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.68213122712422, 91],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.10594547390058, 111],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.060443010546419, 35],\n",
       "       [1, 1, 1, 0, 5, 1.0, 5.521460917862246, 94],\n",
       "       [1, 0, 0, 0, 5, 1.0, 5.231108616854587, 98],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.231108616854587, 110],\n",
       "       [1, 1, 3, 0, 5, 0.0, 4.852030263919617, 41],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.634728988229636, 50],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.429345628954441, 99],\n",
       "       [1, 0, 0, 1, 5, 1.0, 3.871201010907891, 46],\n",
       "       [1, 1, 1, 1, 5, 1.0, 4.499809670330265, 52],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.19295685089021, 102],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.857444178729353, 95],\n",
       "       [0, 1, 0, 1, 5, 0.0, 5.181783550292085, 57],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.147494476813453, 65],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.836281906951478, 39],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.852030263919617, 75],\n",
       "       [1, 1, 2, 1, 5, 1.0, 4.68213122712422, 24],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.382026634673881, 9],\n",
       "       [1, 1, 3, 0, 5, 0.0, 4.812184355372417, 68],\n",
       "       [1, 1, 2, 0, 2, 1.0, 2.833213344056216, 0],\n",
       "       [1, 1, 1, 1, 5, 1.0, 5.062595033026967, 67],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.330733340286331, 21],\n",
       "       [1, 0, 0, 0, 5, 1.0, 5.231108616854587, 113],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.7535901911063645, 18],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.74493212836325, 37],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.852030263919617, 72],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.941642422609304, 78],\n",
       "       [1, 1, 3, 1, 5, 1.0, 4.30406509320417, 8],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.867534450455582, 84],\n",
       "       [1, 1, 0, 1, 5, 1.0, 4.672828834461906, 31],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.857444178729353, 61],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.718498871295094, 19],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.556828061699537, 107],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.553876891600541, 34],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.890349128221754, 74],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.123963979403259, 62],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.787491742782046, 27],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.919980925828125, 108],\n",
       "       [0, 0, 0, 0, 5, 1.0, 5.365976015021851, 103],\n",
       "       [1, 1, 0, 1, 5, 1.0, 4.74493212836325, 38],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.330733340286331, 13],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.890349128221754, 69],\n",
       "       [1, 1, 1, 0, 5, 1.0, 5.752572638825633, 112],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.075173815233827, 73],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.912654885736052, 47],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.204006687076795, 81],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.564348191467836, 60],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.204692619390966, 83],\n",
       "       [0, 1, 0, 0, 5, 1.0, 4.867534450455582, 5],\n",
       "       [1, 1, 2, 1, 5, 1.0, 5.056245805348308, 58],\n",
       "       [1, 1, 1, 1, 3, 1.0, 4.919980925828125, 79],\n",
       "       [0, 1, 0, 0, 5, 1.0, 4.969813299576001, 54],\n",
       "       [1, 1, 0, 1, 4, 1.0, 4.820281565605037, 56],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.499809670330265, 120],\n",
       "       [1, 0, 3, 0, 5, 1.0, 5.768320995793772, 118],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.718498871295094, 101],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.7535901911063645, 26],\n",
       "       [0, 0, 0, 0, 6, 1.0, 4.727387818712341, 33],\n",
       "       [1, 1, 1, 0, 5, 1.0, 6.214608098422191, 119],\n",
       "       [0, 0, 0, 0, 5, 1.0, 5.267858159063328, 89],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.231108616854587, 92],\n",
       "       [1, 0, 0, 0, 6, 1.0, 4.2626798770413155, 6],\n",
       "       [1, 1, 0, 0, 0, 1.0, 4.709530201312334, 90],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.700480365792417, 45],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.298317366548036, 109],\n",
       "       [1, 0, 1, 0, 3, 1.0, 4.727387818712341, 17],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.6443908991413725, 36],\n",
       "       [0, 1, 0, 1, 5, 1.0, 4.605170185988092, 16],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.30406509320417, 7],\n",
       "       [1, 1, 1, 0, 1, 1.0, 5.147494476813453, 88],\n",
       "       [1, 1, 3, 0, 4, 0.0, 5.19295685089021, 87],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.2626798770413155, 3],\n",
       "       [1, 0, 0, 1, 3, 0.0, 4.836281906951478, 59],\n",
       "       [1, 0, 0, 0, 3, 1.0, 5.1647859739235145, 82],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.969813299576001, 66],\n",
       "       [1, 1, 2, 1, 5, 1.0, 4.394449154672439, 51],\n",
       "       [1, 1, 1, 0, 5, 1.0, 5.231108616854587, 100],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.351858133476067, 93],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.605170185988092, 15],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.787491742782046, 106],\n",
       "       [1, 0, 0, 0, 3, 1.0, 4.787491742782046, 105],\n",
       "       [1, 1, 3, 0, 5, 1.0, 4.852030263919617, 64],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.8283137373023015, 49],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.6443908991413725, 42],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.477336814478207, 10],\n",
       "       [1, 1, 0, 1, 5, 1.0, 4.553876891600541, 20],\n",
       "       [1, 1, 3, 1, 3, 1.0, 4.394449154672439, 14],\n",
       "       [1, 0, 0, 0, 5, 1.0, 5.298317366548036, 76],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.90527477843843, 11],\n",
       "       [1, 0, 0, 0, 6, 1.0, 4.727387818712341, 18],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.248495242049359, 23],\n",
       "       [1, 1, 0, 1, 5, 0.0, 5.303304908059076, 63],\n",
       "       [1, 1, 0, 0, 3, 0.0, 4.499809670330265, 48],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.430816798843313, 30],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.897839799950911, 29],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.170483995038151, 86],\n",
       "       [1, 1, 3, 0, 5, 1.0, 4.867534450455582, 115],\n",
       "       [1, 1, 0, 0, 5, 1.0, 6.077642243349034, 116],\n",
       "       [1, 1, 3, 1, 3, 0.0, 4.248495242049359, 40],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.564348191467836, 12]], dtype=object)"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "93c50d44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,\n",
       "       1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1])"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "b7ee351c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "SS=StandardScaler()\n",
    "X_train=SS.fit_transform(X_train)\n",
    "X_test=SS.fit_transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "c5a904f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(criterion='entropy', random_state=0)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "DTClassifier= DecisionTreeClassifier(criterion='entropy' , random_state=0)\n",
    "DTClassifier.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "1b8d4977",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,\n",
       "       1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred= DTClassifier.predict(X_test)\n",
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "59eda05e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The accuracy of decision tree is:  0.7073170731707317\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "print('The accuracy of decision tree is: ', metrics.accuracy_score(y_pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "0a06cb17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB()"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "NBClassifier = GaussianNB()\n",
    "NBClassifier.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "103693a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred= NBClassifier.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "ad1432b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1])"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0853c14c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The accuracy of Naive Bayes is:  0.8292682926829268\n"
     ]
    }
   ],
   "source": [
    "print('The accuracy of Naive Bayes is: ', metrics.accuracy_score(y_pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "2356543e",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata= pd.read_csv(\"loan_data_set.csv.zip\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "c7a84258",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0         NaN             360.0   \n",
       "1             4583             1508.0       128.0             360.0   \n",
       "2             3000                0.0        66.0             360.0   \n",
       "3             2583             2358.0       120.0             360.0   \n",
       "4             6000                0.0       141.0             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  \n",
       "0             1.0         Urban           Y  \n",
       "1             1.0         Rural           N  \n",
       "2             1.0         Urban           Y  \n",
       "3             1.0         Urban           Y  \n",
       "4             1.0         Urban           Y  "
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "b67ff2e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 614 entries, 0 to 613\n",
      "Data columns (total 13 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Loan_ID            614 non-null    object \n",
      " 1   Gender             601 non-null    object \n",
      " 2   Married            611 non-null    object \n",
      " 3   Dependents         599 non-null    object \n",
      " 4   Education          614 non-null    object \n",
      " 5   Self_Employed      582 non-null    object \n",
      " 6   ApplicantIncome    614 non-null    int64  \n",
      " 7   CoapplicantIncome  614 non-null    float64\n",
      " 8   LoanAmount         592 non-null    float64\n",
      " 9   Loan_Amount_Term   600 non-null    float64\n",
      " 10  Credit_History     564 non-null    float64\n",
      " 11  Property_Area      614 non-null    object \n",
      " 12  Loan_Status        614 non-null    object \n",
      "dtypes: float64(4), int64(1), object(8)\n",
      "memory usage: 62.5+ KB\n"
     ]
    }
   ],
   "source": [
    "testdata.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "53a4d88a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender               13\n",
       "Married               3\n",
       "Dependents           15\n",
       "Education             0\n",
       "Self_Employed        32\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount           22\n",
       "Loan_Amount_Term     14\n",
       "Credit_History       50\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "e1ecfc74",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata['Gender'].fillna(testdata['Gender'].mode()[0],inplace=True)\n",
    "testdata['Dependents'].fillna(testdata['Dependents'].mode()[0],inplace=True)\n",
    "testdata['Self_Employed'].fillna(testdata['Self_Employed'].mode()[0],inplace=True)\n",
    "testdata['Loan_Amount_Term'].fillna(testdata['Loan_Amount_Term'].mode()[0],inplace=True)\n",
    "testdata['Credit_History'].fillna(testdata['Credit_History'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "000d778d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender                0\n",
       "Married               3\n",
       "Dependents            0\n",
       "Education             0\n",
       "Self_Employed         0\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount           22\n",
       "Loan_Amount_Term      0\n",
       "Credit_History        0\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "7fd93232",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAGdCAYAAAA44ojeAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA7JklEQVR4nO3dfXhU9Z3//9ckmYwkJhECZJISSTRBqglKoQWhEO4SCqKkXBRXije7dAtFsDFBFNxW6LpBUaKtqVgLKy2u0i0E6tLAJlYMYSMtxKVLEDXSAAIJQYyZ3JEMk/P9g1/OzyGoDFDOIXk+rouLzOe8Z+Z9uK7hvPI5nznHYRiGIQAAABsJsroBAACAcxFQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7YRY3cDFaG9v1/HjxxURESGHw2F1OwAA4AIYhqGGhgbFxcUpKOjL50iuyoBy/PhxxcfHW90GAAC4CB9//LH69ev3pTVXZUCJiIiQdHYHIyMjLe4GwOXk9XpVVFSkjIwMOZ1Oq9sBcBl5PB7Fx8ebx/Evc1UGlI7TOpGRkQQUoIvxer0KCwtTZGQkAQXooi5keQaLZAEAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUAAAgO0QUADYhs/nU0lJiXbs2KGSkhL5fD6rWwJgkYACSkJCghwOR6c/Dz74oKSzNwFaunSp4uLi1KNHD40ZM0b79+/3e43W1lYtWLBAvXv3Vnh4uO666y4dPXr08u0RgKtSQUGBkpKSlJ6erry8PKWnpyspKUkFBQVWtwbAAgEFlN27d6u6utr8U1xcLEn63ve+J0lasWKF8vLylJ+fr927d8vtdis9PV0NDQ3ma2RlZWnTpk1av369du7cqcbGRk2ZMoXflIBurKCgQNOnT1dqaqpKS0v1+uuvq7S0VKmpqZo+fTohBeiOjEvw4x//2LjxxhuN9vZ2o7293XC73cZTTz1lbj99+rQRFRVlvPTSS4ZhGMZnn31mOJ1OY/369WbNsWPHjKCgIGPbtm0X/L719fWGJKO+vv5S2gdgA2fOnDESEhKMO++80/D5fEZbW5uxefNmo62tzfD5fMadd95pJCYmGmfOnLG6VQCXKJDj90XfLLCtrU2vvvqqsrOz5XA49Le//U01NTXKyMgwa1wul9LS0lRWVqY5c+aovLxcXq/XryYuLk4pKSkqKyvTxIkTz/tera2tam1tNR97PB5JZ28q5vV6L3YXANhASUmJDh06pHXr1snn85mf6Y6/H3nkEY0ePVrbt29XWlqala0CuESBHLMvOqBs3rxZn332mR544AFJUk1NjSQpJibGry4mJkaHDx82a0JDQ9WzZ89ONR3PP5/ly5dr2bJlncaLiooUFhZ2sbsAwAZ27NghSTp69KhOnTpljnecQm5paZEkbd26VU1NTVe+QQCXTXNz8wXXXnRAWbNmjSZNmqS4uDi/8XNvoWwYxlfeVvmrahYvXqzs7GzzscfjUXx8vDIyMhQZGXkR3QOwi/DwcOXl5alfv34aNmyYvF6viouLlZ6eLqfTqV27dkmSJk2axAwKcJXrOANyIS4qoBw+fFhvvvmm38I1t9st6ewsSWxsrDleW1trzqq43W61tbWprq7ObxaltrZWI0aM+ML3c7lccrlcncadTqecTufF7AIAmxg7dqwSEhK0YsUKbd682Rx3Op0KDg7WM888o8TERI0dO1bBwcHWNQrgkgVyzL6o66C88sor6tu3r+644w5zLDExUW6325yWlc6uUykpKTHDx5AhQ+R0Ov1qqqurVVFR8aUBBUDXFRwcrJUrV2rLli3KzMzUrl271NLSol27dikzM1NbtmzRs88+SzgBupmAZ1Da29v1yiuv6P7771dIyP//dIfDoaysLOXm5io5OVnJycnKzc1VWFiYZs6cKUmKiorS7NmzlZOTo+joaPXq1UsLFy5UamqqJkyYcPn2CsBVZdq0adqwYYNycnI0evRoczwxMVEbNmzQtGnTLOwOgBUCDihvvvmmjhw5on/6p3/qtG3RokVqaWnRvHnzVFdXp2HDhqmoqEgRERFmzXPPPaeQkBDNmDFDLS0tGj9+vNauXctvR0A3N23aNE2dOlXbt2/X1q1bNWnSJE7rAN2YwzAMw+omAuXxeBQVFaX6+noWyQJdjNfrVWFhoSZPnswaM6CLCeT4zb14AACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQAACA7RBQANiGz+dTSUmJduzYoZKSEvl8PqtbAmARAgoAWygoKFBSUpLS09OVl5en9PR0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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "testdata.boxplot(column='LoanAmount')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "f33634b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Ly8vkZqaKpqampxqLl68KBYuXCh8fX2Fr6+vWLhwoTAajU41jY2NIiUlRXh5eYmAgACxbNky0dPTM+BtYdAhUi4GHSLlcmX/rRJCCPfOKbmPK7d5J6Kbi81mQ1FREebOnctjdIgUxpX9N+91RURERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENERESKxaBDREREisWgQ0RERIrFoENEimO321FWVobDhw+jrKwMdrvd3S0RkZsw6BCRohQUFCAiIgKJiYnIz89HYmIiIiIiUFBQ4O7WiMgNGHSISDEKCgqwYMECREdHo7y8HDt37kR5eTmio6OxYMEChh2iYUglhBDubsJdzGYzJEmCyWSCn5+fu9shokGw2+2IiIhAdHQ09u7dC7vdjqKiIsydOxcajQbp6emor6/H6dOnodFo3N0uEQ2CK/tvzugQkSKUl5fjzJkzeP7556FWO3+1qdVqrF69Gg0NDSgvL3dTh0TkDgw6RKQILS0tAICoqKhrLu8b76sjouGBQYeIFCEkJAQAUF9ff83lfeN9dUQ0PDDoEJEiTJs2DWFhYcjNzYXD4XBa5nA4kJeXh/DwcEybNs1NHRKRO7gUdNauXQuVSuX0T6/Xy8uFEFi7di1CQ0Ph5eWFGTNm4Pjx407rsFgsWL58OQIDA+Hj44N58+bh7NmzTjVGoxGZmZmQJAmSJCEzMxPt7e1ONU1NTUhLS4OPjw8CAwOxYsUKWK1WFzefiJRCo9Fg8+bNKCwsRHp6Oqqrq9Hd3Y3q6mqkp6ejsLAQmzZt4oHIRMOMyzM63//+99HS0iL/O3bsmLxsw4YNyM/Px5YtW3D06FHo9XokJiaio6NDrsnKysKePXtgMBhQUVGBS5cuITU11emCXhkZGairq0NxcTGKi4tRV1eHzMxMebndbkdKSgo6OztRUVEBg8GA3bt3Iycn53rfByJSgPnz52PXrl04duwYpk+fjocffhjTp09HfX09du3ahfnz57u7RSL6rgkXrFmzRtx9993XXOZwOIRerxfr16+Xx3p6eoQkSWLr1q1CCCHa29uF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Nzc7vd7MmTPF6tWrv/6NIiIhhBAe7otYROROp06dwpEjR1BQUAAA8PDwwI9//GP8/ve/x6xZs+S6uLg4+e+AgABERkbik08+kcc8PDycZjXuuusu3Hrrrfjkk09w7733fmMPn3zyCSwWC2bOnPm1Nbt27cKvfvUrfPbZZ7h06RJ6e3v73Y08LCwMvr6+8uOQkBC0tbX9m3fg2iZOnOi0HgBoa2vD6NGjUVdXh8WLF3/ttnh4eCA2NlYeGzlyZL/3y9vbG2PHjpUfBwcHIywsDLfccovTWF//H330EYQQuPPOO51ez2KxYOTIkde1jUTDCYMO0TD15ptvore3F7fddps8JoSAVquF0Wj8xueqVKpvfPx1Y1fz8vL6xuXV1dV46KGHsG7dOiQnJ0OSJBgMBmzevNmpTqvV9ntth8Pxb1//Wq5cV9829K3rm/oVX3M3HSGE03txrV6/qX+HwwGNRoPa2lpoNBqnuivDERFdG4/RIRqGent78cc//hGbN29GXV2d/O8f//gHxowZg7fffluura6ulv82Go349NNPcddddzmt68MPP5Qfnzp1Cu3t7U41X2fcuHHw8vLC+++/f83lH3zwAcaMGYMXXngBkydPxrhx49DY2Ojy9np6ejod3Hu9Jk6c+LW9TpgwAb29vaipqZHHLl68iE8//RTjx4+/7tecNGkS7HY72traEBER4fRPr9df93qJhgvO6BANQ4WFhTAajXj88cchSZLTsgULFuDNN9+UD/j9xS9+gZEjRyI4OBgvvPACAgMDnc6a0mq1WL58OX79619Dq9Vi2bJlmDJlyr/92QoARowYgWeffRarVq2Cp6cn7rvvPpw/fx7Hjx/H448/joiICDQ1NcFgMOAHP/gB9u3bhz179ri8vWFhYaipqcGZM2dwyy23ICAgwOV1AMCaNWswc+ZMjB07Fg899BB6e3uxf/9+rFq1CuPGjcMDDzyAxYsXY9u2bfD19cVzzz2H2267DQ888MB1vR4A3HnnnVi4cCEeeeQRbN68GZMmTcKFCxfw97//HdHR0Zg7d+51r5toOOCMDtEw9Oabb2LWrFn9Qg4A/Od//ifq6urw0UcfAQDWr1+Pp556CjExMWhpacG7774LT09Pud7b2xvPPvssMjIyEBcXBy8vLxgMhgH38uKLLyInJwc///nPMX78ePz4xz+Wj0954IEH8PTTT2PZsmW45557UFlZiRdffNHl7V25ciU0Gg0mTJiA733ve9d9vaAZM2bgr3/9K959913cc889uP/++51mcLZv346YmBikpqYiLi4OQggUFRX1+2nKVdu3b8cjjzyCnJwcREZGYt68eaipqfnGs8eI6DKV+LofloloWDt06BASEhJgNBq/9gJ/O3bsQFZWFtrb27/T3oiIBoozOkRERKRYDDpERESkWPzpioiIiBSLMzpERESkWAw6REREpFgMOkRERKRYDDpERESkWAw6REREpFgMOkRERKRYDDpERESkWAw6REREpFgMOkRERKRY/x8hzaEqIygOsQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "testdata.boxplot(column='ApplicantIncome')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "4db99e3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata.LoanAmount= testdata.LoanAmount.fillna(testdata.LoanAmount.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "03932d8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata['LoanAmount_log']=np.log(testdata['LoanAmount'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "51d3990f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID              0\n",
       "Gender               0\n",
       "Married              3\n",
       "Dependents           0\n",
       "Education            0\n",
       "Self_Employed        0\n",
       "ApplicantIncome      0\n",
       "CoapplicantIncome    0\n",
       "LoanAmount           0\n",
       "Loan_Amount_Term     0\n",
       "Credit_History       0\n",
       "Property_Area        0\n",
       "Loan_Status          0\n",
       "LoanAmount_log       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "e6cafad1",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata['TotalIncome']= testdata['ApplicantIncome']+testdata['CoapplicantIncome']\n",
    "testdata['TotalIncome_log']= np.log(testdata['TotalIncome'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "1ca8bb1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "      <th>LoanAmount_log</th>\n",
       "      <th>TotalIncome</th>\n",
       "      <th>TotalIncome_log</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>146.412162</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.986426</td>\n",
       "      <td>5849.0</td>\n",
       "      <td>8.674026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "      <td>4.852030</td>\n",
       "      <td>6091.0</td>\n",
       "      <td>8.714568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.189655</td>\n",
       "      <td>3000.0</td>\n",
       "      <td>8.006368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.787492</td>\n",
       "      <td>4941.0</td>\n",
       "      <td>8.505323</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.948760</td>\n",
       "      <td>6000.0</td>\n",
       "      <td>8.699515</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0  146.412162             360.0   \n",
       "1             4583             1508.0  128.000000             360.0   \n",
       "2             3000                0.0   66.000000             360.0   \n",
       "3             2583             2358.0  120.000000             360.0   \n",
       "4             6000                0.0  141.000000             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  LoanAmount_log  TotalIncome  \\\n",
       "0             1.0         Urban           Y        4.986426       5849.0   \n",
       "1             1.0         Rural           N        4.852030       6091.0   \n",
       "2             1.0         Urban           Y        4.189655       3000.0   \n",
       "3             1.0         Urban           Y        4.787492       4941.0   \n",
       "4             1.0         Urban           Y        4.948760       6000.0   \n",
       "\n",
       "   TotalIncome_log  \n",
       "0         8.674026  \n",
       "1         8.714568  \n",
       "2         8.006368  \n",
       "3         8.505323  \n",
       "4         8.699515  "
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "8d410193",
   "metadata": {},
   "outputs": [],
   "source": [
    "test= testdata.iloc[:,np.r_[1:5,9:11,13:15]].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "57dc6c78",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0,5):\n",
    "    test[:,i]=labelencoder_X.fit_transform(test[:,i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "558c700f",
   "metadata": {},
   "outputs": [],
   "source": [
    "test[:,7]=labelencoder_X.fit_transform(test[:,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "daefd380",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 0, ..., 1.0, 4.986425672954842, 320],\n",
       "       [1, 1, 1, ..., 1.0, 4.852030263919617, 333],\n",
       "       [1, 1, 0, ..., 1.0, 4.189654742026425, 42],\n",
       "       ...,\n",
       "       [1, 1, 1, ..., 1.0, 5.53338948872752, 436],\n",
       "       [1, 1, 2, ..., 1.0, 5.231108616854587, 416],\n",
       "       [0, 0, 0, ..., 0.0, 4.890349128221754, 185]], dtype=object)"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "5c3e830a",
   "metadata": {},
   "outputs": [],
   "source": [
    "test= SS.fit_transform(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "9149a7d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred= NBClassifier.predict(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "64d4a45b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,\n",
       "       0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,\n",
       "       0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,\n",
       "       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,\n",
       "       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,\n",
       "       0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4d39828",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
