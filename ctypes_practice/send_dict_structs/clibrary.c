#include <stdio.h>
 
// struct Point {
//     int x;
//     int y;
//     //float z;
// };

struct InputParams
{
    double RadIncrement;
    double BoxSize;          
    double MaxRadiusSearch;  
    double ProxyGridSize;  
    double FracRadius;       
    double DeltaThreshold;   
    double DeltaSeed;        
    double OverlapTol;   
    double Redshift;         
    double OmegaMatter;
    double OmegaLambda;
    double Hubble;  
    double FidOmegaMatter;        
    double FidOmegaLambda;        
    double FidHubble;  
    double MinProfileDist;   
    double MaxProfileDist;   
    double ScalePos;
    double ScaleVel;
    double InnerShellVel;  
    double OuterShellVel; 

    int    FormatTracers;
    int    NumFiles;
    int    NumRanWalk;
    int    OMPcores;         
    int    RSDist;           
    int    GDist;                     
    int    WriteProfiles;        
    int    NumProfileBins;       
    //int    RunFlag;
};


int main(){
    return 0;
}
 
// void printPoint(struct Point p) {
//         //printf("%.2f\n",p.z);
//         printf("%d %d\n", p.x, p.y);
// }

void load_input_file(struct InputParams input)
{
printf("%.2f\n", input.RadIncrement);
printf("%.2f\n", input.BoxSize);
printf("%.2f\n", input.MaxRadiusSearch);
printf("%.2f\n", input.ProxyGridSize);
printf("%.2f\n", input.FracRadius);
printf("%.2f\n", input.DeltaThreshold);
printf("%.2f\n", input.DeltaSeed);
printf("%.2f\n", input.OverlapTol);

printf("%.2f\n", input.Redshift);
printf("%.2f\n", input.OmegaMatter);
printf("%.2f\n", input.OmegaLambda);
printf("%.2f\n", input.Hubble);
printf("%.2f\n", input.FidOmegaMatter);
printf("%.2f\n", input.FidOmegaLambda);
printf("%.2f\n", input.FidHubble);
printf("%.2f\n", input.MinProfileDist);
printf("%.2f\n", input.MaxProfileDist);
printf("%.2f\n", input.InnerShellVel);
printf("%.2f\n", input.OuterShellVel);

printf("%d\n", input.FormatTracers);
printf("%d\n", input.NumFiles);
printf("%d\n", input.NumRanWalk);
printf("%d\n", input.OMPcores);
printf("%d\n", input.RSDist);
printf("%d\n", input.GDist);
printf("%d\n", input.WriteProfiles);
printf("%d\n", input.NumProfileBins);
  
}