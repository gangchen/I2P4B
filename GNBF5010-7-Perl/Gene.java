
public class Gene extends GeneticElement{
	String geneSymbol;
	int geneid;
	
	public Gene(String s, int id, int c, int p){
		
		geneSymbol = s;
		geneid = id;
		
		if(c > 23){
			System.out.println("The chr number is wrong!");
		}
		chr = c;
		pos = p;
	}
	
	public Gene(){
		
	}
	
}
