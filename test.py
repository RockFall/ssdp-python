import ssdp
s = ssdp.SSDP(target="positive")
p = s.run(10, "QR")


# If the file name contains:
#  freq_2
#  freq_4
#  freq_8
#  width_2
#  width_4
#  width_8
# Then we save internally the
# discretization type used on the data

#def _check_prior_discretization():
#    if "freq_2" in 

"""
public static void CarregarArquivo(String caminho, int tipoArquivo) throws FileNotFoundException{
          
        if(caminho.contains("freq_2")){
            D.tipoDiscretizacao = Const.TIPO_BASE_FREQ2;
        }else if(caminho.contains("freq_4")){
            D.tipoDiscretizacao = Const.TIPO_BASE_FREQ4;
        }else if(caminho.contains("freq_8")){
            D.tipoDiscretizacao = Const.TIPO_BASE_FREQ8;
        }else if(caminho.contains("width_2")){
            D.tipoDiscretizacao = Const.TIPO_BASE_WIDTH2;
        }else if(caminho.contains("width_4")){
            D.tipoDiscretizacao = Const.TIPO_BASE_WIDTH4;
        }else if(caminho.contains("width_8")){    
            D.tipoDiscretizacao = Const.TIPO_BASE_WIDTH8;
        }else{
            D.tipoDiscretizacao = "Não discretizada";
        }
        
        String[][] dadosStr = null;
        switch(tipoArquivo){
            case D.TIPO_CSV:
                dadosStr = D.CVStoDadosStr(caminho);
        }
        D.dadosStrToD(dadosStr);
        
        D.numeroItensUtilizados = D.numeroItens;
        D.itensUtilizados = new int[D.numeroItensUtilizados];
        for(int l = 0; l < D.numeroItensUtilizados; l++){
            D.itensUtilizados[l] = l;
        }
        Pattern.vrPCount = new int[D.numeroExemplosPositivo];
        Pattern.vrNCount = new int[D.numeroExemplosNegativo];
    }
    
    
    //Lendo arquivo no formato padrão
        D.caminho = caminho;
        Scanner scanner = new Scanner(new FileReader(D.caminho))
                       .useDelimiter("\\n");
        ArrayList<String[]> dadosString = new ArrayList<>();        
              
        
        String[] palavras = D.caminho.split("\\\\");
        if(palavras.length == 1){
            palavras = D.caminho.split("/");//Caso separador de pastas seja / e  não \\
        }
        
        D.nomeBase = palavras[palavras.length-1].replace(".CSV", "");//Nome do arquivo é a última palavra
        
        
        D.nomeVariaveis = scanner.next().split(D.SEPARADOR); //1º linha: nome das variáveis
        D.numeroAtributos = D.nomeVariaveis.length-1; //último atributo é o rótulo
        while (scanner.hasNext()) {
            dadosString.add(scanner.next().split(D.SEPARADOR));
        }
        D.numeroExemplos = dadosString.size();
        
        String[][] dadosStr = new String[D.numeroExemplos][D.numeroAtributos+1];
        for(int i = 0; i < dadosString.size(); i++){
            String[] exemploBase = dadosString.get(i);//recebe linha de dados
            for(int j = 0; j < exemploBase.length; j++){
                dadosStr[i][j] = exemploBase[j];
            }            
        }       
        
        return dadosStr;
    
    
    """
