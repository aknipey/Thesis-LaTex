import os

content = r"""\documentclass[12pt]{article}

\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{setspace}
\usepackage{graphicx}
\usepackage{float}
\usepackage{tabularx}
\usepackage{fancyhdr}
\usepackage{xcolor} % For grey footer
\usepackage[hidelinks]{hyperref}
\usepackage{longtable}
\usepackage{array}
\usepackage{booktabs}
\usepackage[utf8]{inputenc}
% Use biblatex for reference management
\usepackage[backend=biber,style=ieee]{biblatex}
% \addbibresource{References.bib} % Uncomment and create References.bib to use

% Header and Footer setup
\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot[L]{\textcolor{gray}{\thepage}}
\fancyfoot[C]{\textcolor{gray}{A. Knipe, Thesis Progress Report}}
\renewcommand{\headrulewidth}{0pt} % remove header rule
\renewcommand{\footrulewidth}{0pt} % remove footer rule

% Section numbering style (Roman)
\renewcommand{\thesection}{\Roman{section}}

\begin{document}
\pagenumbering{roman} % Start roman numerals
\onehalfspacing

% --- Title Page ---
\begin{titlepage}
    \begin{center}
        \begin{figure}[H] 
            \centering 
            % \includegraphics[width=7cm]{Figures/UNSW Logo.jpg} % Uncomment when logo is available
            \vspace{3cm} % Placeholder for logo
        \end{figure}
        
        \LARGE
        School of Mechanical and Manufacturing Engineering \\
        
        Faculty of Engineering \\

        UNSW Sydney

        \vspace{0.25cm}
        
        \LARGE
        BY \\
        \vspace{0.25cm}
        
        \huge
        \textbf{Aidan Knipe} \\
        \vspace{0.5cm}
        
        \LARGE
        \textbf{Macro-Micro Robotic System with a Flexible Continuum Tip for Minimally Invasive Surgery}
        \vspace{0.5cm}
        
        \LARGE
        Thesis submitted as a requirement for the degree of Bachelor of Engineering in Mechatronic Engineering
        \vspace{0.5cm}

        \large
        \begin{tabularx}{1\textwidth}{ 
  | >{\raggedright\arraybackslash}X 
  | >{\raggedright\arraybackslash}X 
  | } 
        \hline
        Submitted: \today & Student zID: [Your zID] \\ 
        \hline
        Supervisor: Dr. Liao Wu (UNSW) & \\ 
        \hline
        \end{tabularx}
    \end{center}
\end{titlepage}

\newpage
% --- Abstract ---
\begin{abstract}
This draft literature review is structured for a thesis on a UR5e-based macro-micro robotic system with a flexible continuum tip for minimally invasive surgery (MIS). It consolidates relevant findings from prior work in the \textit{Lachlan Report}, identifies which foundations remain valid, and highlights where the state of the art now requires updated evidence. The review prioritizes four technical threads central to this thesis: (1) tendon-driven continuum manipulator design and motion algorithms, (2) integration with a macro robot (UR5e), (3) collision detection and avoidance for safe operation in constrained anatomy, and (4) rapid end-effector exchange mechanisms. It also includes explicit ``missing area'' headings to direct next-stage searching, reading, and synthesis.
\end{abstract}

\newpage
% --- Originality Statement ---
\section*{ORIGINALITY STATEMENT}
\addcontentsline{toc}{section}{Originality Statement}

\textit{`I hereby declare that this submission is my own work and to the best of my knowledge it contains no materials previously published or written by another person, or substantial proportions of material which have been accepted for the award of any other degree or diploma at UNSW or any other educational institution, except where due acknowledgement is made in the thesis. Any contribution made to the research by others, with whom I have worked at UNSW or elsewhere, is explicitly acknowledged in the thesis. I also declare that the intellectual content of this thesis is the product of my own work, except to the extent that assistance from others in the project's design and conception or in style, presentation and linguistic expression is acknowledged.'} \\

\vspace{1cm}
Signed: \rule{5cm}{0.4pt} \\

\vspace{1cm}
Date: \hspace{0.1cm} \rule{5cm}{0.4pt}

\newpage
% --- Table of Contents, Figures, Tables ---
\tableofcontents
\newpage
\listoffigures
\addcontentsline{toc}{section}{List of Figures}
\newpage
\listoftables
\addcontentsline{toc}{section}{List of Tables}

\newpage
% --- Nomenclature ---
\section*{Nomenclature}
\addcontentsline{toc}{section}{Nomenclature}
\textit{(The nomenclature must respect the following order: latin symbols, Greek symbols, acronyms. Within each category of symbols, follow alphabetic order. An example is provided below)}

\vspace{0.5cm}
\begin{tabular}{>{\raggedright}p{2cm} c p{10cm}}
$A$ & = & amplitude of \dots \\
$C_p$ & = & \dots \\
$C_x$ & = & \dots \\
$C_y$ & = & \dots \\
$D$ & = & \dots \\
$\alpha$ & = & \dots \\
TLA & = & \dots \\
\end{tabular}

\newpage
% --- Main Body Sections ---
\pagenumbering{arabic} % Switch to arabic numbering from Introduction

\section{Introduction}
\subsection{Project Context and Problem Significance}
This thesis extends prior macro-micro robotic surgery work by coupling a UR5e macro manipulator with a new flexible continuum tip, then improving movement algorithms inherited from earlier implementations. The applied significance is strong: MIS demands dexterity in constrained spaces, low tissue interaction force, high positional repeatability, and robust safety controls.

From the earlier project, the macro-micro concept and teleoperation feasibility are already established at a proof-of-concept level. The key opportunity now is to move from demonstration toward a more clinically credible engineering argument through stronger modeling, safety layers (especially collision handling), and modular hardware architecture (rapid tool exchange).

\subsection{Working Thesis Gap Statement (Draft)}
Current literature and prior project work support feasibility of macro-micro MIS manipulation, but leave a practical translation gap at the intersection of \textbf{accurate continuum movement control}, \textbf{real-time collision-safe operation}, and \textbf{fast, repeatable end-effector reconfiguration}. This thesis addresses that gap on a UR5e-based platform by improving inherited motion algorithms and integrating safety and modularity mechanisms necessary for repeatable experimental deployment.

\section{Literature Review}

\subsection{Introduction to Minimally Invasive Surgery (MIS) and Robotics}
\begin{itemize}
    \item The clinical motivation: Why do we need surgical robots? (Precision, dexterity, patient outcomes).
    \item The rise of Macro-Micro systems (combining a large positioning arm like a UR5e with a delicate continuum tip).
\end{itemize}

\subsection{Teleoperation and Control in Surgical Robotics}
\begin{itemize}
    \item \textit{The Problem:} Human tremor, system latency, and mapping user intent to rigid vs. continuum kinematics.
    \item \textit{Current Solutions:} Review papers on teleoperation filters (Kalman filters, moving average, predictive kinematics).
    \item \textit{The Gap:} Discuss how high-end systems do this well, but open-source/low-cost systems (like Lachlan's) suffer from vibratory feedback across ROS/external control nodes.
\end{itemize}

\subsection{Modularity and Tendon-Driven Continuum Manipulators}
\begin{itemize}
    \item \textit{The Problem:} Continuum robots are excellent for navigating complex anatomies, but they are usually monolithic. If a tool breaks or a different tip is needed, the whole robot is swapped.
    \item \textit{Current Solutions:} Review mechanical coupling techniques in robotics (magnetic tool changers, mechanical twist-locks).
    \item \textit{The Gap:} Analyze the specific challenge of maintaining tendon tension across a boundary. Why hasn't a quick-release mechanism been widely adopted for micro-continuum robots yet?
\end{itemize}

\subsection{Safety and Haptic Boundaries (The "Lane Assist")}
\begin{itemize}
    \item \textit{Brief Review:} Virtual fixtures, active constraints, and force estimation in MIS.
    \item \textit{Context:} How this ties into the motion smoothing—if the robot knows where \textit{not} to go, the predictive algorithm can correct the user's path safely.
\end{itemize}

\subsection{Summary and Research Gap Identification}
\begin{itemize}
    \item A concise section explicitly stating the limitations of current low-cost systems (specifically citing Lachlan's baseline report) and formulating how your thesis will address the vibrating control and hardware rigidity.
\end{itemize}

\subsection*{Additional Planning}
% Everything from the previous Lit Review sections mapped under this unnumbered heading
\subsubsection*{Inherited Knowledge from Lachlan Report: What Is Still Useful}
The prior report remains highly relevant in these areas.
\paragraph{Continuum and Snake-like Design Foundations}
The prior review appropriately positioned tendon-driven continuum/snake-like manipulators as a practical and dominant pathway for surgical dexterity. The classification of continuum architectures and the design trade-off framing (dexterity, stiffness, manufacturability, miniaturization) remain useful to retain.
\paragraph{Macro-Micro Integration Rationale}
The macro-micro argument is still strong: a rigid macro arm contributes workspace and gross positioning, while a flexible micro tip contributes distal dexterity and safer interaction in confined regions. This directly aligns with using the UR5e as the macro stage and a continuum tip as the micro stage.
\paragraph{Teleoperation and Controller Pipeline Lessons}
The earlier implementation experience (ROS integration, latency considerations, and vibration observations) provides practical system-level lessons for architecture and control-loop design. Even if this thesis shifts focus from pure teleoperation toward autonomy-assisted control, these integration lessons are still relevant.
\paragraph{Kinematic Modeling as a Bottleneck}
The prior work highlighted that continuum-tip performance quality is tightly linked to model quality and calibration quality. That finding should be retained as a central thesis narrative point: movement algorithm improvement must be justified through both model structure and validation methodology.

\subsubsection*{What Must Be Brought Up to Date}
The earlier literature base appears strongest through roughly 2022 and should now be updated in the following directions.
\paragraph{Post-2022 Continuum Manipulator Control}
Update with recent results on:
\begin{itemize}
    \item Data-driven and learning-augmented continuum control (model correction, residual learning).
    \item Real-time model-based control under friction, hysteresis, and tendon coupling.
    \item Multi-objective control formulations balancing tracking error, smoothness, and safety constraints.
\end{itemize}
\paragraph{Safety-Critical Surgical Robot Control}
The inherited report discusses precision and teleoperation, but safety layers should now be treated as first-class control objectives:
\begin{itemize}
    \item Constraint-aware motion planning and control barrier function style methods.
    \item Contact-aware control and force-limited behavior near anatomical boundaries.
    \item Fault handling and safe-stop behavior for software and communication faults.
\end{itemize}
\paragraph{Collision Detection and Avoidance (Core Gap for This Thesis)}
This is one of the most important expansion areas for your project. The review needs a dedicated synthesis of:
\begin{itemize}
    \item Geometric collision detection for continuum bodies (not just rigid-link approximations).
    \item Environment representations (point cloud, mesh, signed distance field) suitable for intraoperative updates.
    \item Real-time avoidance strategies compatible with UR5e + continuum-tip control bandwidth.
\end{itemize}
\paragraph{Rapid End-Effector Change and Modular Interfaces}
The prior conclusion already identifies end-effector replacement as cumbersome. This thesis should elevate this into an explicit engineering research stream:
\begin{itemize}
    \item Mechanical quick-change couplers for sterile or semi-sterile workflows.
    \item Repeatable kinematic/electrical interface registration after each swap.
    \item Calibration and safety checks needed after end-effector exchange.
\end{itemize}

\subsubsection*{Focused Literature Synthesis for Current Thesis Objectives}
\paragraph{Thread A: Continuum Tip Design for MIS on UR5e}
The review should compare tendon-driven continuum options based on criteria directly linked to your implementation:
\begin{itemize}
    \item Outer diameter and achievable curvature.
    \item Tendon routing complexity and friction sensitivity.
    \item Manufacturability (3D printing route, assembly complexity, tolerance sensitivity).
    \item Instrument channel requirements and compatibility with intended tasks.
\end{itemize}

\paragraph{Thread B: Movement Algorithm Improvement over Lachlan Baseline}
Define baseline algorithm(s) from inherited work, then review candidate improvements under consistent metrics:
\begin{itemize}
    \item Tracking performance (RMS error, peak error, settling behavior).
    \item Robustness to tendon slack, backlash, and parameter drift.
    \item Computational feasibility for real-time execution.
\end{itemize}
The literature section should explicitly map each candidate algorithm class to likely implementation effort and expected gain.

\paragraph{Thread C: Collision Detection and Avoidance in Constrained Anatomy}
Your review should separate the problem into three layers:
\begin{itemize}
    \item \textbf{Perception/model layer}: what representation of anatomy and instruments is available in real time?
    \item \textbf{Detection layer}: how are self-collision, tool-environment collision, and forbidden regions detected?
    \item \textbf{Response layer}: how does the controller react (hard stop, velocity scaling, local re-plan, haptic/visual warning)?
\end{itemize}

\paragraph{Thread D: Rapid End-Effector Exchange}
This thread should connect mechanism design with control and safety:
\begin{itemize}
    \item Mechanical interchange design options and locking reliability.
    \item Coupling repeatability and resulting pose uncertainty.
    \item Required post-swap validation routine before re-entry into operation.
\end{itemize}

\subsubsection*{Explicit Missing Research Areas (Add These as Search Targets)}
\begin{itemize}
    \item \textbf{Missing Area 1:} Benchmark Datasets and Standardized Evaluation Protocols for Continuum Surgical Robots.
    \item \textbf{Missing Area 2:} Real-Time Collision Avoidance Methods Validated on Macro-Micro Systems with Flexible Distal Tools.
    \item \textbf{Missing Area 3:} Registration Drift and Recalibration After Quick End-Effector Exchange.
    \item \textbf{Missing Area 4:} Safety Cases for Human-in-the-Loop MIS Robots with Shared Control.
    \item \textbf{Missing Area 5:} Tendon Wear, Sterilization Effects, and Lifecycle Reliability in Reconfigurable Continuum Tools.
    \item \textbf{Missing Area 6:} Task-Specific Performance Metrics Beyond Tip Tracking Error.
\end{itemize}

\section{Research Question and Project Plan}

\subsection{Thesis Question \& Aims}
\textbf{Proposed Thesis Question:} \\
\textit{"How can predictive motion smoothing algorithms and modular hardware interfaces be integrated into a low-cost macro-micro continuum robotic system to improve teleoperation precision and reduce end-effector exchange times during minimally invasive surgery?"}

\textbf{Primary Aims:}
\begin{enumerate}
    \item \textbf{Algorithmic:} Develop and evaluate a software-side predictive motion smoothing or filtering algorithm to eliminate translational vibrations in the teleoperation of the macro arm (UR5e).
    \item \textbf{Mechanical:} Design and prototype a rapid-exchange mechanism (e.g., magnetic or twist-lock) for the 4mm tendon-driven continuum tip that maintains necessary tendon routing and tension.
    \item \textbf{Validation (If time permits/Idea 2 integration):} Validate the improved precision and safety of the system, potentially incorporating a preliminary haptic or visual "lane-assist" boundary condition (collision avoidance) to protect delicate tissues.
\end{enumerate}

\subsection{Project Plan Alignment}
Your final report should ensure the plan is narratively tied to the review:
\begin{itemize}
    \item Each project task should be justified by a gap identified in this section.
    \item Include feasible milestones and contingency options (especially for hardware delays and calibration issues).
\end{itemize}

\subsection{Proposed Next Reading and Writing Sequence}
\begin{enumerate}
    \item Build a paper matrix with columns: method class, hardware platform, control rate, collision strategy, modularity strategy, metrics, limitations.
    \item Fill collision-avoidance and quick-change sections first (highest novelty for your topic).
    \item Revisit inherited movement algorithm section and position your planned improvement as a direct response to documented limitations.
    \item Close the review with a concise ``identified gap to thesis objective'' mapping table.
\end{enumerate}

\section{Project Dependent Preparations}
The literature should foreshadow practical preparations you can evidence:
\begin{itemize}
    \item UR5e safety/process training,
    \item software stack readiness,
    \item preliminary prototype tests,
    \item risk register for collision and tool-swap failure modes.
\end{itemize}

\section{Conclusion}
\textit{Conclusion content to be written.}

\newpage
% --- Acknowledgements ---
\pagenumbering{Alph} % Switch numbering to Alphabetic

\section*{Acknowledgements}
\addcontentsline{toc}{section}{Acknowledgements}
\textit{I would like to thank...}

\newpage
% --- References ---
% To compile references, you will need to run pdflatex -> biber -> pdflatex -> pdflatex
% \printbibliography[heading=bibintoc, title={References}]
\section*{References}
\addcontentsline{toc}{section}{References}
\textit{(To be populated using BibLaTeX and Biber)}

\newpage
% --- Appendices ---
\appendix
\addcontentsline{toc}{section}{Appendices}
\section{Rubric-Aligned Coverage Notes (MMAN4951/MMAN9451 Interim Report)}
\subsection*{Criterion 1: Literature Review (High Weighting)}
To target Distinction/High Distinction bands, this review must do more than summarize papers. It should:
\begin{itemize}
    \item Show conceptual links between manipulator design, control, safety, and modularity.
    \item Explicitly identify and justify knowledge gaps your thesis addresses.
    \item Include recent work (not only foundational papers).
    \item Critically compare methods instead of listing them.
\end{itemize}

\subsection*{Criterion 4: Document Presentation}
For marks protection, maintain:
\begin{itemize}
    \item consistent citation formatting,
    \item clear figure/table captions,
    \item polished grammar and structured argument flow.
\end{itemize}

\end{document}
"""

with open('Lit Review/Lit Review.tex', 'w', encoding='utf-8') as f:
    f.write(content)
