import javax.swing.JOptionPane;


public class Zahlenratespiel {
	
	public static void main(String[] args) {
		float generierteZahl = (float) Math.random() * 100;
		int zufaeligeZahl = (int) generierteZahl;
		String eingabe = JOptionPane.showInputDialog("Gib eine Zahl ein");
		int tipp = Integer.parseInt(eingabe);
		
		while(tipp != zufaeligeZahl) {
			if(tipp < zufaeligeZahl) {
				JOptionPane.showMessageDialog(null, "Deine Zahl ist kleiner als die gesuchte Zahl");
				eingabe = JOptionPane.showInputDialog("Gib eine neuen Tipp ab!");
				tipp = Integer.parseInt(eingabe);
			} else if(tipp > zufaeligeZahl) {
				JOptionPane.showMessageDialog(null, "Deine Zahl ist größer als die gesuchte Zahl");
				eingabe = JOptionPane.showInputDialog("Gib eine neuen Tipp ab!");
				tipp = Integer.parseInt(eingabe);
				
			}
		}
		
		JOptionPane.showMessageDialog(null, "Dein Tipp war richtig! Die gesuchte Zahl war " + zufaeligeZahl);
	}
}
