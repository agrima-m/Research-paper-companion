from crewai import Agent
from crewai_tools import PDFSearchTool

# Load the PDF tool
pdf_tool = PDFSearchTool(pdf='paper.pdf')

# Topic Explainer
explainer = Agent(
    role="Topic Explainer",
    goal="Explain complex technical ideas in simple terms",
    backstory="An expert science communicator and educator",
    tools=[pdf_tool],
    verbose=True
)

# Literature Finder
literature_agent = Agent(
    role="Literature Finder",
    goal="Find related works or previously published research",
    backstory="A research librarian skilled at academic literature discovery",
    tools=[pdf_tool],
    verbose=True
)

# Gap Analyzer
gap_analyzer = Agent(
    role="Gap Analyzer",
    goal="Identify research gaps or open questions in the paper",
    backstory="A critical analyst with a deep understanding of scientific research",
    tools=[pdf_tool],
    verbose=True
)
