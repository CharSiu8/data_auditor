# main.py is the director
import auditor
import reporter
import analyzer

def main():
    target_file = 'test_data.csv'

    print("Step 1: Auditing...") 
    # Runs logic in Auditor
    results = auditor.run_audit(target_file)

    print("Step 2: Saving Report...")
    # This sends that dictionary to reporter.py to save as JSON
    reporter.generate_report(results)

    print("Step 3: AI is Analyzing...")
    # This tells analyzer.py to read the JSON and talk to OpenAI
    # We pass the filename 'audit_summary.json' as the instruction
    ai_summary = analyzer.analyze_audit_results('audit_summary.json')
    
    print("\n" + "="*30)
    print("OpenAI-Powered Analysis")
    print("="*30)
    print(ai_summary)
    print("="*30)

# The ignition switch
if __name__ == "__main__":
    main()