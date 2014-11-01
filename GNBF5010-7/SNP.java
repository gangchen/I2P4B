
public class SNP extends GeneticElement{
	String rsid;
	String comment;

	public SNP(String s, int c, int p, String co ){
		rsid = s;
		chr = c;
		pos = p;
		comment = co;
	}
	
	public SNP(){
		
	}

}
