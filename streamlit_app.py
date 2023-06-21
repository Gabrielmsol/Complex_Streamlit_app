import streamlit as st                                                                                                                              
from complex import *                                                                                                                               
import matplotlib.pyplot as plt                                                                                                                     
import sympy as sp

# Text structure

Title = 'Complex viewer'                                                                                                                            
subsection = 'What is going on ?'                                                                                                                   
explanation = 'You might have learnt about complex numbers in the past, have the thought\n' \                                                       
              'ever cross your mind, how does these numbers portray in certain functions?\n' \                                                      
              'These amazing visuals are never shown over, even in college subjects as\n' \                                                         
              'complex variables, only the behaviors are studied and in some simple cases\n' \                                                      
              'we can try visualizing, since depending on function, understanding the image\n' \                                                    
              'might be very troublesome.'

subsection1 = 'Visualizing the complex plane'                                                                                                       
explanation1 = 'This that you see beneath is the complex plane with no function applied.\n' \                                                       
               'Places with lighter color are closer to the center, those with darker have\n' \                                                     
               'a bigger module.'

subsection2 = 'Applying a function to our complex plane.'                                                                                           
explanation2 = 'Now that we are familiarized with the complex plane, we can see the beauty\n' \                                                     
               'behind said transformations.\n' \                                                                                                   
               'Please keep in mind that lighter colors used to be close to the center of our plane\n' \                                            
               'and darker further away.'                                                                                                           
text2 = 'Lets see some functions'                                                                                                                   
explanation2_1 = 'This is one of my personal favorites, this is what happens when you apply\n' \                                                    
                 "Newton's method to a polynomial function with 5 symmetrical roots one time. "                                                     
latex2_1 = r'\displaystyle{f(z) = z-\frac{z^5-1}{5\ z^4}}'                                                                                          
explanation2_2 = 'Another beautiful function is the sin function applied to itself 7 times'                                                         
latex_2_2 = r'\displaystyle{f(z) = \sin(\sin(\ldots\sin(z)))}'

subsection3 = 'Try for yourself'                                                                                                                    
text3 = 'Now that you are familiarized you can try your own functions.'

# end

                                                                                                                                                    
# Functions

def newton(z):                                                                                                                                      
    return z - (z**5-1)/(5*z**4)

                                                                                                                                                    
def sin7(z):                                                                                                                                        
    for i in range(7):                                                                                                                              
        z = np.sin(z)                                                                                                                               
    return z

                                                                                                                                                    
def plot_graph(function, grid, size):                                                                                                               
    if grid is not None:

        cmap = np.abs(grid)                                                                                                                         
        tensor = get_tensor(function(grid))                                                                                                         
        tensor[..., 1] = cmap                                                                                                                       
        x, y = get_dimensions(tensor)

        plt.style.use('dark_background')                                                                                                            
        fig, ax = plt.subplots()                                                                                                                    
        plot = st.pyplot(fig)                                                                                                                       
        ax.scatter(x, y, s=1, c=np.real(tensor[..., 1].flatten()), cmap='inferno_r')                                                                
        ax.set_xlim(-size, size)                                                                                                                    
        ax.set_ylim(-size, size)                                                                                                                    
        ax.set_aspect('equal')                                                                                                                      
        plot.pyplot(fig)

                                                                                                                                                    
def box_for_sqr_or_cir():                                                                                                                           
    with st.form('key1'):                                                                                                                           
        sqr_or_cir = st.radio('Do you prefer to see the complex plane as a in Euler form or rather have it all filled?',                            
                              ('Clear', 'Euler', 'Square'))                                                                                         
        st.form_submit_button('Submit')

    if sqr_or_cir == 'Clear':                                                                                                                       
        return None                                                                                                                                 
    if sqr_or_cir == 'Euler':                                                                                                                       
        return make_circ(0, 1, 0, 2*np.pi, 100, 500)                                                                                                
    if sqr_or_cir == 'Square':                                                                                                                      
        return make_grid(-1, 1, 223, 223)

                                                                                                                                                    
def box_for_yourself():                                                                                                                             
    with st.form('key2'):                                                                                                                           
        sqr_or_cir = st.radio('Do you prefer to see the complex plane as a in Euler form or rather have it all filled?',                            
                              ('Clear', 'Euler', 'Square'))                                                                                         
        size = st.number_input('Enter the size that you wish to visualize your graph.\n'                                                            
                               'Tip around 1 is pretty good.\n'                                                                                     
                               'if you get to choose Euler configuration, this will give the radi.')                                                
        number_r = st.number_input('Enter how many points you want on the Real axis and Imaginary.\n'                                               
                                   'Detail, if you choose Euler configuration, these will be points in the direction of the radi.\n'                
                                   'Tip avoid using too many points, under 250 is usually good.', value=0, step=1, format="%d")                     
        number_w = st.number_input('If you choose Euler configuration, this will serve as points in the angle direction.\n '                        
                                   'Tip avoid using too many points, under 300 is usually good.', value=0, step=1, format="%d")                     
        Function = st.text_input('Enter your function here:\n'                                                                                      
                                 'Please refer to your variable as z, use computer notation. Ex:\n'                                                 
                                 'sin(z)**z+exp(z)+cos(z)/12*12')                                                                                   
        Function = Function.replace('^','**').replace('e**z', 'sp.exp(z)').replace('e**(', 'sp.exp(')\                                              
            .replace('sin', 'sp.sin').replace('cos', 'sp.cos').replace('exp', 'sp.exp')

        st.form_submit_button('plot it')

    z = sp.symbols('z')                                                                                                                             
    ld = {'np': np, 'z': z, 'sp': sp}                                                                                                               
    if sqr_or_cir == 'Clear'\                                                                                                                       
            or number_r == 0:                                                                                                                       
        return None                                                                                                                                 
    if sqr_or_cir == 'Euler'\                                                                                                                       
            and number_w == 0:                                                                                                                      
        return None                                                                                                                                 
    if sqr_or_cir == 'Euler'\                                                                                                                       
            and number_w != 0:                                                                                                                      
        Function = eval(Function, {}, ld)                                                                                                           
        f = sp.lambdify(z, Function, modules=['numpy'])                                                                                             
        grid = make_circ(0, size, 0, 2*np.pi, number_r, number_w)                                                                                   
        plot_graph(f, grid, size*1.2)                                                                                                               
    if sqr_or_cir == 'Square':                                                                                                                      
        Function = eval(Function, {}, ld)                                                                                                           
        f = sp.lambdify(z, Function, modules=['numpy'])                                                                                             
        grid = make_grid(-size, size, number_r, number_w)                                                                                           
        plot_graph(f, grid, size*1.2)

                                                                                                                                                    
# end

                                                                                                                                                    
# Site structure

st.title(Title)                                                                                                                                     
st.subheader(subsection)                                                                                                                            
st.text(explanation)

st.subheader(subsection1)                                                                                                                           
st.text(explanation1)                                                                                                                               
grid = box_for_sqr_or_cir()                                                                                                                         
plot_graph(Z, grid, 1.2)

st.subheader(subsection2)                                                                                                                           
st.text(explanation2)                                                                                                                               
st.text(text2)                                                                                                                                      
st.text(explanation2_1)                                                                                                                             
st.latex(latex2_1)                                                                                                                                  
plot_graph(newton, grid, 1.2)                                                                                                                       
st.text(explanation2_2)                                                                                                                             
st.latex(latex_2_2)                                                                                                                                 
plot_graph(sin7, grid, 1.2)

st.subheader(subsection3)                                                                                                                           
st.text(text3)                                                                                                                                      
box_for_yourself()

# end
