{
 "cells": [
  {
   "cell_type": "raw",
   "id": "1ad72fee",
   "metadata": {},
   "source": [
    "#Write a Python function to sum all the numbers in a list.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "41882380",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "def sum(number_of_list):\n",
    "    total_sum = 0\n",
    "    for x in number_of_list:\n",
    "        total_sum += x\n",
    "    return total_sum\n",
    "\n",
    "print(sum((8,2,3,0,7)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b4688dc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff90741c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a Python program to reverse a string.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "66219e54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'dcba4321'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def reverse(string):\n",
    "    if len(string) == 0:\n",
    "        return string\n",
    "    else:\n",
    "        return reverse(string[1:]) + string[0]\n",
    "\n",
    "reverse(\"1234abcd\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc24ae55",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "162be733",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a Python function that accepts a string and calculate the number \n",
    "#of upper case letters and lower case letters.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "233370fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any string:\tThe quick Brow Fox\n",
      "The number of uppercase character is:\n",
      "3\n",
      "The number of lowercase character is:\n",
      "12\n"
     ]
    }
   ],
   "source": [
    "any_letter=input(\"enter any string:\\t\")\n",
    "count_lower=0\n",
    "count_upper=0\n",
    "\n",
    "for i in any_letter:\n",
    "    if(i.islower()):\n",
    "        count_lower=count_lower+1\n",
    "    elif(i.isupper()):\n",
    "        count_upper=count_upper+1\n",
    "        \n",
    "print(\"The number of uppercase character is:\")\n",
    "print(count_upper)\n",
    "print(\"The number of lowercase character is:\")\n",
    "print(count_lower)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26b997aa",
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
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
