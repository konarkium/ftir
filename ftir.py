import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

#fix font to 14 and make it so it's editable PDF
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14

#grab data
filename = 'ftir.csv'
df = pd.read_csv(filename)

#pull data from CSV
x = df['waveno'].dropna()
ySA = df['SA'].dropna()
ymel = df['mel'].dropna()

ypre2 = df['pre2'].dropna()
yMF2 = df['MF2'].dropna()
yMFC2 = df['MFC2'].dropna()

ypre4 = df['pre4'].dropna()
yMF4 = df['MF4'].dropna()
yMFC4 = df['MFC4'].dropna()

ypre6 = df['pre6'].dropna()
yMF6 = df['MF6'].dropna()
yMFC6 = df['MFC6'].dropna()

#Set the limits of the plot
xmin = 500
xmax = 4100

#Prepare multipanel plot 
fig = plt.figure(1, figsize=(10, 14))
#prepare grid
gs = gridspec.GridSpec(18,5)
#determine gap dimentions
gs.update(hspace=0.0005)

#%% SA

xtr_subplot = fig.add_subplot(gs[15,0:5])

plt.xlim([xmax, xmin]) #limits are set from 4500 to 500 to invert the x axis data points 

dict_SA = dict(zip(x,ySA))

for key,value in dict_SA.items():
    if 0.849 < value < 0.96:
        plt.axvline(x=key, color = 'blue', alpha = 0.05)
    elif value < 0.849:
        plt.axvline(x=key, color = 'blue')

plt.plot(x, ySA, label = 'SA', color = 'blue')

plt.text(480,0.875,'SA')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(labelbottom=False, labeltop=False, 
                labelright=False, labelleft=False)

#%% melamine
 
xtr_subplot = fig.add_subplot(gs[17,0:5])

plt.xlim([xmax, xmin]) #limits are set from 4500 to 500 to invert the x axis data points

dict_mel = dict(zip(x,ymel))

for key,value in dict_mel.items():
    if 0.935 < value < 0.97:
        plt.axvline(x=key, color = 'yellow', alpha = 0.08)
    elif value < 0.935:
        plt.axvline(x=key, color = 'yellow')


plt.plot(x, ymel, label = 'mel', color = 'yellow')

plt.text(480,0.96,'mel.')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(labelbottom=True, labeltop=False, 
                labelright=False, labelleft=False)

plt.xlabel(r'Wavenumber [cm$^-$$^1$]')

#%% comparing pre-polymers

xtr_subplot = fig.add_subplot(gs[0:4,0:5])

plt.xlim([xmax, xmin]) #limits are set from 4500 to 500 to invert the x axis data points 

plt.plot(x, ypre2, label = 'MFP2.5', linestyle = 'dotted',color = 'orange')
plt.plot(x, ypre4+0.1, label = 'MFP4.5', linestyle = 'dashed', color = 'orange')
plt.plot(x, ypre6+0.2, label = 'MFP6.5', color = 'orange')
plt.legend(loc='lower center')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(labelbottom=False, labeltop=False, 
                labelright=False, labelleft=False)

for key,value in dict_mel.items():
    if value < 0.935:
        plt.axvline(x=key, color = 'yellow', alpha = 0.1)

#%% comparing resins

xtr_subplot = fig.add_subplot(gs[5:9,0:5])

plt.xlim([xmax, xmin]) #limits are set from 4500 to 500 to invert the x axis data points 

plt.plot(x, yMF2, label = 'MFR2.5', linestyle = 'dotted', color = 'red') 
plt.plot(x, yMF4+0.025, label = 'MFR4.5', linestyle = 'dashed', color = 'red') 
plt.plot(x, yMF6+0.05, label = 'MFR6.5', color = 'red') 
plt.legend(loc='lower center')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(labelbottom=False, labeltop=False, 
                labelright=False, labelleft=False)

for key,value in dict_mel.items():
    if value < 0.935:
        plt.axvline(x=key, color = 'yellow', alpha = 0.1)
        
plt.ylabel(r'$\leftarrow$ Transmittance [%] $\rightarrow$')

#%% comparing microcapsules

xtr_subplot = fig.add_subplot(gs[10:14,0:5])

plt.xlim([xmax, xmin]) #limits are set from 4500 to 500 to invert the x axis data points 

plt.plot(x, yMFC2, label = 'MFC2.5', linestyle = 'dotted', color = 'purple')
plt.plot(x, yMFC4+0.0125, label = 'MFC4.5', linestyle = 'dashed', color = 'purple')
plt.plot(x, yMFC6+0.025, label = 'MFC6.5', color = 'purple')
plt.legend(loc='lower center')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=True, left=False, right=False)
plt.tick_params(labelbottom=False, labeltop=False, 
                labelright=False, labelleft=False)

for key,value in dict_mel.items():
    if value < 0.935:
        plt.axvline(x=key, color = 'yellow', alpha = 0.1)
        
for key,value in dict_SA.items():
    if value < 0.849:
        plt.axvline(x=key, color = 'blue', alpha = 0.05)

#%%

plt.savefig('ftir.png', dpi=300,bbox_inches="tight")


































 