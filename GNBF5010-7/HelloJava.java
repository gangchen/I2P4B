
public class HelloJava {
	public static void main(String[] args){
		//SNP s = new SNP("SNP", "rs671", 12, 12);
		
		GeneticElement ge = new GeneticElement();
		
		Gene g = new Gene("TP53", 7157, 17, 7668402);
		
		Gene g1 = new Gene("FOT", 7273, 25, 2323223);
		
		SNP s = new SNP("rs671", 6, 2323, "Alchol dep");
		
		System.out.println(g.geneSymbol);
		System.out.println(g.pos);
		System.out.println(g.getPos());
		System.out.println(s.pos);
	}
}
