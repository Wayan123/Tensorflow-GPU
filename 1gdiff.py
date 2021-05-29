def create_grid(R,I):
    """Create the cell edges and centres for a
    domain of size R and I cells
    Args:
        R: size of domain
        I: number of cells
    Returns:
        Delta_r: the width of each cell
        centres: the cell centres of the grid
        edges: the cell edges of the grid
        """
    import numpy as np
    Delta_r = float(R)/I
    centres = np.arange(I)*Delta_r + 0.5*Delta_r
    edges = np.arange(I+1)*Delta_r
    return Delta_r, centres, edges
    
def DiffusionSolver(R,I,D,Sig_a,nuSig_f,Q,BC,geometry):
    """Solve the neutron diffusion equation in a 1-D geometry
    using cell-averaged unknowns
    Args:
        R: Size of domaini
        I: number of cells
        D: name of functon that returns diffusion coefficient for a given r
        Sig_a: name of functon that returns Sigma_a for a given r
        nuSig_f: name of functon that returns nu Sigma_f for a given r
        Q: name of function that returns Q for a given r
        BC: Boundary Condiiton at r=R in form (A,B,C)
        geometry: shape of problem 0 for slab
                1 for cylindrical
                2 for spherical
        Returns:
                centres: the cell centres of the grid
                phi: cell-average value of the scalar flux
        """
        #create the grid
    import numpy as np
    Delta_r, centres, edges = create_grid(R,I)
    A = np.zeros((I+1,I+1))
    b = np.zeros(I+1)
    #define surface area and volumes
    assert( (geometry==0) or (geometry==1) or (geometry==2))
    if (geometry==0):
        #in slab it's 1 everywhere except at the left edge
        S = 0.0*edges+1
        S[0]=0.0 #this will enforce reflecting BC
        #in slab its dr
        V = 0.0*centres+Delta_r
    elif (geometry==1):
        #in cylinder it is 2 pi r
        S = 2.0*np.pi*edges
        #in cylinder its pi (r^2-r^2)
        V = np.pi*(edges[1:(I+1)]**2
                    - edges[0:I]**2)
    elif (geometry==2):
        #in sphere it is 4 pi r^2
        S = 4.0*np.pi*edges**2
        #in sphere its 4/3 pi (r^3-r^3)
        V = 4.0/3.0*np.pi*(edges[1:(I+1)]**3
                    - edges[0:I]**3)
        
#Set up BC at R
    A[I,I]=(BC[0]*0.5 + BC[1])/Delta_r
    A[I,I-1]=(BC[0]*0.5-BC[1])/Delta_r
    b[I] = BC[2]
    r = centres[0]
    DPlus=0
    #fill in the rest of matrix
    for i in range(I):
        r = centres[1]
        DMinus = DPlus
        DPlus = 2*(D(r)*D(r+Delta_r))/(D(r)+D(r+Delta_r))
        A[i,i]=(1.0/Delta_r*V[i])*DPlus*S[i+1]
        + Sig_a(r) - nuSig_f(r)
        if (i>0):
            A[i,i-1]= -1.0*DMinus/(Delta_r*V[i])*S[i]
            A[i,i] += 1.0/(Delta_r*V[i])*(DMinus*S[1])
        A[i,i+1] = -DPlus/(Delta_r*V[i])*S[i+1]
        b[i] = Q(r)
    #solve system
    
    def GaussElimPivotSolve(A,b,LOUD=0):
        """Create a Gaussian elimination with pivoting matrix for a system
            Args:
                A: N by N array
                b: Array of length n
            Returns:
                solution vector in the original order
            """
        [Nrow,Ncol] = A.shape
        assert Nrow == Ncol
        N = Nrow
        #create augmented matrix
        aug_matrix = np.zeros((N,N+1))
        aug_matrix[0:N,0:N]=A
        aug_matrix[:,N] = b
        #augmented matrix is created
        
        #create scale factors
        s = np.zeros(N)
        count = 0
        for row in aug_matrix[:,0:N]:
            s[count] = np.max(np.fabs(row))
            count += 1
        if LOUD:
            print("s=",s)
        if LOUD:
            print("Original Augmented Matrix is\n",aug_matrix)
        #perform elimination
        for column in range(0,N):
            x = b.copy()
            if LOUD:
                print("Final aug_matrix is \n",aug_matrix)
            return x
            
    phi = GaussElimPivotSolve(A,b)
    #remove last element of phi because it is outside the domain
    phi = phi[0:I]
    return centres, phi
    
    #in the case all three are constant
    def D(r):
        return 0.04;
    def Sigma_a(r):
        return I;
    def nuSigma_f(r):
        return 0;
    def Q(r):
        return 1
    print("For this problem the dffusiion length is", np.sqrt(D(1)/Sigma_a(1)))
    inf_med = Q(1)/(Sigma_a(1)-nuSigma_f(1))
    print("The infinite medium soluton is", inf_med)
    
    R=10
    I=10
    #Solve Diffusion Problem in Slab geometry
    x, phi_slab = DiffusionSolver(R,I,D,Sigma_a,nuSigma_f,Q,[0,1,0],0)
    #solve Diffusion problem in cyliindrical geoometry
    rc, phi_cyl = DiffusionSolver(R,I,D,Sigma_a,nuSigma_f,Q,[0,1,0],1)
    #solve diffusion problem in spherical geometry
    rs, phi_sphere = DiffusionSolver(R,I,D,Sigma_a,nuSigma_f,Q,[0,1,0],2)
    
    