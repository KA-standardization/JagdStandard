#include "md5.h"
#include <iostream>

using namespace std;

void PrintMD5(const string &str, MD5 &md5) {
    cout << "MD5(\"" << str << "\")=" << md5.toString() << endl;
}

string FileDigest(const string& file) {

    ifstream in(file.c_str(), ios::binary);
    if (!in)
        return "";

    MD5 md5;
    std::streamsize length;
    char buffer[1024];
    while (!in.eof()) {
        in.read(buffer, 1024);
        length = in.gcount();
        if (length > 0)
            md5.update(buffer, length);
    }
    in.close();
    return md5.toString();
}

int main() {
    MD5 md5;
    md5.update("101_3_2.0+/api/v4/members/chang-shou-92/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cexcerpt%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.vessay_info%3Bdata%5B*%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B*%5D.author.vip_info%3Bdata%5B*%5D.question.has_publishing_draft%2Crelationship&offset=0&limit=20&sort_by=created+\"AHDfF6dC5xOPTl6HxDtnrscCQ1xlAFvFJDM=|1634717134\"+3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7T9yr6nxeTtqXRFZSTrZgcO9kUS_IHkmWgLBpukYWgxmIQPYqbpfZUnPS0FZG0Yq-6C1ZhSYVCxm1uV_70RqSMCBVuky16P0riRCyufOovxBXgSCiiR0ELYuUrxmtDomqU7ynXtOnAoTh_PhRDSTFMcmCqSMBXOmugpKfqLs0DxqZcH0kGHqTre1crxGfHCmtCOKfhXL9he_M9STvirGSHOsbHNYsiSBOJV8kDe1k9pqYcSqyGQ_kML_pU20fXLLicOChUXmyUHYQCCyfGe_fBg869cYQBxmCqOfSgCB0BNmsQH_i9SVqGxBkRFKMAS_YwXmOqkw67CfhggMOgOKqGSfr7Nm6UFKuruKbBNso0xywgFqeXSLT9O9S4LL7gVYrUu0Tg2pwJO1nqYMzhuBScHxIutMuJSMfCH_PDcVtCSBlJO0QQVfwweK-BHC");
    PrintMD5("1613960752", md5);
    return 0;
}